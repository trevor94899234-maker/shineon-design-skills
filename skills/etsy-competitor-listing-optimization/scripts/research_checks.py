#!/usr/bin/env python3
"""Offline structural guardrails. Never claims semantic truth or makes external writes."""
import argparse
import hashlib
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

AGE = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?|\.\d+)\s*(years?|yrs?|y|months?|mos?|mo|m)\b', re.I)
KINDS = {'research_only', 'listing_draft', 'authorized_application'}
CLAIM_TYPES = {'recipient','sender','buyer','writer','eventual_reader','deceased','material','process','occasion','other'}
LIMITS = [
    'Structural checks do not establish semantic accuracy, source authenticity, demand, profit, or qualification sufficiency.',
    'Source byte integrity is checked only when --source-root is supplied.',
    'Independent semantic audit and visual/openability checks require separate evidence.'
]

def nonblank(x):
    return isinstance(x,str) and bool(x.strip())

def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)

def timestamp(x):
    try:
        return bool(isinstance(x,str) and datetime.fromisoformat(x.replace('Z','+00:00')).utcoffset() is not None)
    except (TypeError, ValueError):
        return False

def parse_age(raw):
    """Parse a dedicated Etsy duration field, not arbitrary page prose."""
    if not isinstance(raw, str) or not raw.strip():
        return {'raw': raw, 'years': None, 'status': 'missing'}
    text = ' '.join(raw.split())
    hits = list(AGE.finditer(text))
    if not hits or len(hits) > 2:
        return {'raw': raw, 'years': None, 'status': 'needs_review'}
    # Reject numeric leftovers, signs, alternative/range phrasing, or two same-unit claims.
    rest = AGE.sub('', text)
    if re.search(r'\d|[-+~–—]|\bor\b|\bto\b|\babout\b|\bunder\b|\bover\b', rest, re.I):
        return {'raw': raw, 'years': None, 'status': 'needs_review'}
    units = ['y' if h[2].lower().startswith('y') else 'm' for h in hits]
    if len(hits) == 2 and (units != ['y','m'] or float(hits[1][1]) >= 12):
        return {'raw': raw, 'years': None, 'status': 'needs_review'}
    # Only the dedicated display grammar is accepted; sentences need human reading.
    if re.sub(r'\bon\s+Etsy\b|\band\b|\s+|[,()]', '', rest, flags=re.I):
        return {'raw': raw, 'years': None, 'status': 'needs_review'}
    years = sum(float(h[1]) / (12 if u == 'm' else 1) for h,u in zip(hits,units))
    return {'raw': raw, 'years': round(years,8), 'status': 'display_duration', 'exact_opening_date': None}

def canonical_listing(value):
    if isinstance(value, str) and re.fullmatch(r'\d+',value):
        return 'etsy:listing:'+value
    if not isinstance(value,str): return None
    p=urlparse(value)
    if p.scheme not in ('https','http') or (p.hostname or '').lower() not in {'etsy.com','www.etsy.com'}:
        return None
    m=re.match(r'^/(?:[a-z]{2}/)?listing/(\d+)(?:/|$)', p.path)
    return 'etsy:listing:'+m[1] if m else None

def risk_flags(text):
    """Review prompts only. No material or role classification is produced."""
    if not isinstance(text,str): return []
    rules = {
        'negation': r'\b(?:not|never|without|no)\b',
        'option_or_conditional': r'\b(?:optional|option|can|could|if|choose|select)\b',
        'quoted_language': r'["“”‘’]|\b(?:quote|phrase|wording)\b',
        'multiple_product_targets': r'\b(?:pen|packaging|pages|box|bundle)\b',
        'grief_or_deceased': r'\b(?:grief|grieving|memorial|memory of|deceased|loss of|late father)\b',
        'relationship_roles': r'\b(?:from|to|for|daughter|son|mother|father|mom|dad|sister|friend)\b'
    }
    return [k for k,v in rules.items() if re.search(v,text,re.I)]

def inventory_report(bundle):
    run=bundle.get('run',{}); pages=bundle.get('inventory_pages',[]); errors=[]
    if not isinstance(run,dict): return {'complete':False,'errors':['run must be an object']}
    if not isinstance(pages,list) or any(not isinstance(p,dict) for p in pages): return {'complete':False,'errors':['inventory_pages must be an array of objects']}
    source_rows=bundle.get('sources',[])
    if not isinstance(source_rows,list): return {'complete':False,'errors':['sources must be an array']}
    source_ids={s.get('source_id') for s in source_rows if isinstance(s,dict) and isinstance(s.get('source_id'),str)}
    seen_pages=set(); ids=[]; previous=None; previous_ids=None
    snapshot=run.get('inventory_snapshot_id')
    if pages and (not isinstance(snapshot,str) or not snapshot.strip()): errors.append('Missing nonempty inventory snapshot ID')
    for p in pages:
        key=p.get('page_key')
        if not isinstance(key,str): errors.append('page_key must be a string'); key=str(key)
        if not isinstance(p.get('source_id'),str) or p.get('source_id') not in source_ids: errors.append('Unresolved inventory source at '+str(key))
        if not key or key in seen_pages: errors.append('Missing or repeated page_key: '+str(key))
        seen_pages.add(key)
        if p.get('previous_page_key') != previous: errors.append('Broken page chain at '+str(key))
        if p.get('snapshot_id') != snapshot: errors.append('Snapshot mismatch at '+str(key))
        if not timestamp(p.get('observed_at')): errors.append('Missing timezone timestamp at '+str(key))
        rawids=p.get('listing_ids',[])
        if not isinstance(rawids,list) or any(not isinstance(i,str) or not i.isdigit() for i in rawids):
            errors.append('Invalid listing IDs at '+str(key)); rawids=[]
        if previous is not None and rawids and rawids == previous_ids:
            errors.append('Repeated inventory content at '+str(key))
        ids.extend(rawids); previous=key; previous_ids=rawids
    unique=len(set(ids)); expected=run.get('inventory_expected')
    if expected is not None and (not isinstance(expected,int) or isinstance(expected,bool) or expected<0): errors.append('Invalid expected inventory count')
    if expected is not None and unique != expected: errors.append('Unique count does not reconcile to expected count')
    displayed=set()
    for p in pages:
        count=p.get('displayed_count')
        if count is not None:
            if not isinstance(count,int) or isinstance(count,bool) or count<0: errors.append('Invalid displayed inventory count')
            else: displayed.add(count)
    if pages and not displayed: errors.append('No source-displayed count; expected count alone cannot establish completeness')
    if len(displayed)>1 or (expected is not None and displayed and displayed!={expected}): errors.append('Conflicting displayed inventory counts')
    requested=run.get('inventory_stop') != 'not_requested'
    if requested and not pages: errors.append('No inventory pages captured')
    complete=requested and bool(pages) and expected is not None and run.get('inventory_stop')=='verified_end' and not errors
    return {'complete':complete,'page_count':len(pages),'captured_card_count':len(ids),'unique_listing_count':unique,'duplicate_cards':len(ids)-unique,'expected':expected,'errors':errors,'coverage':'complete_snapshot' if complete else 'partial_or_not_requested'}

def validate(b, source_root=None):
    errors=[]; warnings=[]
    # Fail closed on malformed container shapes before following references.
    for name in ['run','qa']:
        if not isinstance(b.get(name),dict): errors.append(f'{name} must be an object')
    arrays=['sources','shops','listings','metrics','claims','inventory_pages','qualifications','keywords','corrections','social_accounts']
    for name in arrays:
        if not isinstance(b.get(name),list) or any(not isinstance(x,dict) for x in b.get(name,[])):
            errors.append(f'{name} must be an array of objects')
    if errors: return {'passed':False,'errors':errors,'warnings':[],'limitations':LIMITS}
    for source in b['sources']:
        if not isinstance(source.get('text'),dict): errors.append('source.text must be an object')
    for name,fields in {'qualifications':['comparable_claim_ids','relevant_product_evidence_ids','success_metric_ids'], 'keywords':['source_ids','metric_ids'], 'social_accounts':['identity_evidence_source_ids']}.items():
        for row in b[name]:
            for field in fields:
                if field in row and (not isinstance(row[field],list) or any(not isinstance(v,str) for v in row[field])): errors.append(f'{name}.{field} must be an array of string IDs')
    qa=b['qa']
    for name in ['errors_by_category','category_audit_complete']:
        if not isinstance(qa.get(name,{}),dict): errors.append(f'qa.{name} must be an object')
    for name in ['audited_categories','expanded_categories','output_checks']:
        if not isinstance(qa.get(name,[]),list): errors.append(f'qa.{name} must be an array')
    if errors: return {'passed':False,'errors':errors,'warnings':[],'limitations':LIMITS}
    for row in b['sources']:
        if any(not isinstance(v,str) for v in row['text'].values()): errors.append('source.text values must be exact strings')
    for name,fields in {'shops':['source_id'],'listings':['source_id','shop_key'],'metrics':['source_id','entity_key'],'claims':['source_id','entity_key'],'corrections':['entity_key'],'social_accounts':['shop_key']}.items():
        for row in b[name]:
            for field in fields:
                if not isinstance(row.get(field),str): errors.append(f'{name}.{field} must be a string reference')
    for cat,n in qa.get('errors_by_category',{}).items():
        if not isinstance(n,int) or isinstance(n,bool) or n<0: errors.append(f'qa.errors_by_category.{cat} must be a nonnegative integer')
    if errors: return {'passed':False,'errors':errors,'warnings':[],'limitations':LIMITS}
    def err(msg): errors.append(msg)
    def required(row, fields, label):
        for f in fields:
            if f not in row or row[f] is None or row[f]=='': err(f'{label}: missing {f}')
    def index(name,key):
        rows=b.get(name,[])
        if not isinstance(rows,list): err(f'{name} must be an array'); return {}
        result={}
        for i,r in enumerate(rows):
            if not isinstance(r,dict): err(f'{name}[{i}] must be object'); continue
            k=r.get(key)
            if not isinstance(k,str): err(f'{name}: {key} must be a string'); continue
            if not k or k in result: err(f'{name}: missing/duplicate {key} {k!r}')
            if k: result[k]=r
        return result
    if b.get('schema_version')!='1.0': err('Unsupported schema_version')
    run=b.get('run',{})
    required(run,['run_id','mode','stage','buyer_country','currency','language','collected_at','target_decision'],'run')
    if run.get('mode') not in KINDS: err('Invalid run mode')
    if run.get('stage') not in {'draft','delivery'}: err('Invalid run stage')
    if not timestamp(run.get('collected_at')): err('run.collected_at needs timezone')
    sources=index('sources','source_id'); shops=index('shops','shop_key'); listings=index('listings','listing_key')
    metrics=index('metrics','metric_id'); claims=index('claims','claim_id'); keywords=index('keywords','keyword_id')
    qualifications=index('qualifications','shop_key'); index('corrections','correction_id')
    entities=set(shops)|set(listings)
    for sid,s in sources.items():
        required(s,['source_url','captured_at','method','market_scope','raw_file','sha256'],sid)
        if not timestamp(s.get('captured_at')): err(f'{sid}: captured_at needs timezone')
        if not isinstance(s.get('text'),dict): err(f'{sid}: text must be a source-field map')
        if not re.fullmatch(r'[0-9a-f]{64}',str(s.get('sha256',''))): err(f'{sid}: invalid sha256')
        if source_root:
            root=Path(source_root).resolve(); path=(root/str(s.get('raw_file',''))).resolve()
            if path!=root and root not in path.parents: err(f'{sid}: raw_file escapes source root'); continue
            if not path.is_file(): err(f'{sid}: raw file unavailable'); continue
            if hashlib.sha256(path.read_bytes()).hexdigest()!=s.get('sha256'): err(f'{sid}: raw hash mismatch')
    def source_check(r,label):
        if not isinstance(r.get('source_id'),str) or r.get('source_id') not in sources: err(f'{label}: unresolved source_id')
    for key,s in shops.items():
        source_check(s,key)
        if not nonblank(s.get('shop_name')): err(f'{key}: shop_name must be a nonempty string')
        if s.get('shop_id') is not None and not isinstance(s.get('shop_id'),str): err(f'{key}: shop_id must be a string or null')
        if not timestamp(s.get('observed_at')): err(f'{key}: observed_at needs timezone')
        if not re.fullmatch(r'etsy:shop:(\d+)|etsy:shopname:[^\s]+',key): err(f'{key}: invalid shop key')
        if key.startswith('etsy:shop:') and str(s.get('shop_id'))!=key.rsplit(':',1)[1]: err(f'{key}: shop ID/key mismatch')
        if s.get('age_years') is not None:
            parsed=parse_age(s.get('age_raw'))
            if parsed['years'] is None or not number(s['age_years']) or abs(parsed['years']-s['age_years'])>1e-7: err(f'{key}: age does not match full raw duration')
    for key,l in listings.items():
        source_check(l,key)
        if not timestamp(l.get('observed_at')): err(f'{key}: observed_at needs timezone')
        for field in ['title','description','tags','tags_provenance','comparator_class','selected','detail_captured','price_raw','price','currency','variant','quantity','shipping_raw','shipping_cost','shipping_scope']:
            if field not in l: err(f'{key}: missing field {field}; use null for unknown')
        for field in ['selected','detail_captured']:
            if not isinstance(l.get(field),bool): err(f'{key}: {field} must be boolean')
        if l.get('comparator_class') not in {'direct','adjacent','excluded'}: err(f'{key}: invalid comparator_class')
        if canonical_listing(l.get('listing_id'))!=key: err(f'{key}: listing identity mismatch')
        if l.get('shop_key') not in shops: err(f'{key}: unresolved shop_key')
        if l.get('tags') is not None and (not isinstance(l.get('tags'),list) or any(not isinstance(v,str) for v in l.get('tags',[]))): err(f'{key}: tags must be string array or null')
        for field in ['title','description','tags_provenance','currency','variant','shipping_scope']:
            if l.get(field) is not None and not isinstance(l[field],str): err(f'{key}: {field} must be string or null')
        for field in ['price','shipping_cost']:
            if l.get(field) is not None and (not number(l[field]) or l[field]<0): err(f'{key}: {field} must be a finite nonnegative number or null')
        if l.get('quantity') is not None and (not isinstance(l['quantity'],int) or isinstance(l['quantity'],bool) or l['quantity']<1): err(f'{key}: quantity must be a positive integer or null')
        if l.get('tags') and not l.get('tags_provenance'): err(f'{key}: missing tag provenance')
        if l.get('visual_inspected') is True and l.get('visual_verified') is not True: err(f'{key}: visual inspection needs explicit true verification')
    for mid,m in metrics.items():
        source_check(m,mid); required(m,['metric','status','entity_scope','period','market_scope','definition'],mid)
        if m.get('status') not in {'observed','estimated','missing','unavailable','conflict'}: err(f'{mid}: invalid metric status')
        if m.get('entity_scope') not in {'shop','listing','query'}: err(f'{mid}: invalid metric scope')
        if m.get('entity_scope')=='shop' and m.get('entity_key') not in shops: err(f'{mid}: shop scope must reference a shop')
        if m.get('entity_scope')=='listing' and m.get('entity_key') not in listings: err(f'{mid}: listing scope must reference a listing')
        if m.get('entity_scope')!='query' and m.get('entity_key') not in entities: err(f'{mid}: unresolved entity')
        if m.get('status') in {'missing','unavailable'} and m.get('value') is not None: err(f'{mid}: missing/unavailable must be null, not zero')
        if m.get('value') is not None and not number(m['value']): err(f'{mid}: nonfinite/non-numeric value')
        if m.get('metric')=='shop_sales_cumulative' and (m.get('entity_scope')!='shop' or m.get('period') not in {'lifetime','as_displayed','lifetime_displayed'}): err(f'{mid}: shop cumulative sales scope/period mismatch')
        raw=str(m.get('raw_value','')).strip()
        if raw.startswith('<') and m.get('qualifier')!='less_than': err(f'{mid}: lost less-than qualifier')
        if raw.startswith('>') and m.get('qualifier')!='greater_than': err(f'{mid}: lost greater-than qualifier')
        if re.search(r'erank|everbee',str(sources.get(m.get('source_id'),{}).get('method','')),re.I) and re.search(r'sales|revenue',str(m.get('metric','')),re.I) and m.get('status')=='observed': err(f'{mid}: third-party sales/revenue must remain estimated')
    for cid,c in claims.items():
        source_check(c,cid)
        if c.get('status') not in {'supported','unknown','conflict','hypothesis'}: err(f'{cid}: invalid claim status')
        if c.get('entity_key') not in entities: err(f'{cid}: unresolved entity')
        if c.get('claim_type') not in CLAIM_TYPES: err(f'{cid}: invalid claim_type')
        if c.get('status')=='supported':
            required(c,['quote','source_field','polarity','target','reviewer','reviewed_at'],cid)
            source_text=sources.get(c.get('source_id'),{}).get('text',{}).get(c.get('source_field'))
            if not isinstance(source_text,str) or not c.get('quote') or c['quote'] not in source_text: err(f'{cid}: quote not exact in referenced source field')
            if c.get('polarity') not in {'positive','negative','conditional','quoted','unknown'}: err(f'{cid}: invalid polarity')
            if not timestamp(c.get('reviewed_at')): err(f'{cid}: reviewed_at needs timezone')
            if risk_flags(c.get('quote')): warnings.append(f'{cid}: semantic risk requires independent review: '+','.join(risk_flags(c['quote'])))
    def owner(entity):
        return entity if entity in shops else listings.get(entity,{}).get('shop_key')
    for key,q in qualifications.items():
        if key not in shops: err(f'{key}: qualification lacks shop')
        if q.get('status') not in {'well_supported','provisional','candidate','adjacent','excluded'}: err(f'{key}: invalid qualification status')
        for field in ['comparable_claim_ids','relevant_product_evidence_ids']:
            for cid in q.get(field,[]):
                if cid not in claims: err(f'{key}: unresolved {field} {cid}')
                elif owner(claims[cid].get('entity_key'))!=key: err(f'{key}: evidence {cid} belongs to another shop')
        for mid in q.get('success_metric_ids',[]):
            if mid not in metrics: err(f'{key}: unresolved success metric {mid}')
            elif owner(metrics[mid].get('entity_key'))!=key: err(f'{key}: success metric {mid} belongs to another shop')
        if q.get('status')=='well_supported':
            for field in ['comparable_claim_ids','relevant_product_evidence_ids','success_metric_ids','rationale','caveats','reviewed_at']:
                if not q.get(field): err(f'{key}: well_supported requires {field}')
            for cid in q.get('comparable_claim_ids',[])+q.get('relevant_product_evidence_ids',[]):
                if claims.get(cid,{}).get('status')!='supported': err(f'{key}: qualification claim is not supported')
    for kid,k in keywords.items():
        for sid in k.get('source_ids',[]):
            if sid not in sources: err(f'{kid}: unresolved source')
        for mid in k.get('metric_ids',[]):
            if mid not in metrics: err(f'{kid}: unresolved metric')
        if k.get('metric_ids') and k.get('provenance')!='measured_exact_query': err(f'{kid}: observed tag/wording cannot inherit demand metrics')
        if k.get('decision') in {'accept','reject','hold'} and not k.get('decision_reason'): err(f'{kid}: missing decision reason')
    for correction in b.get('corrections',[]):
        cid=correction.get('correction_id')
        if correction.get('entity_key') not in entities: err(f'{cid}: correction has unresolved entity')
        if not isinstance(correction.get('source_ids'),list) or not correction.get('source_ids'): err(f'{cid}: correction needs source_ids')
        else:
            for sid in correction['source_ids']:
                if not isinstance(sid,str) or sid not in sources: err(f'{cid}: correction has unresolved source')
        for field in ['field','before','after','quote','reason','reviewer','corrected_at','affected_outputs']:
            if field not in correction: err(f'{cid}: correction missing {field}')
        if not timestamp(correction.get('corrected_at')): err(f'{cid}: correction timestamp needs timezone')
    for i,a in enumerate(b.get('social_accounts',[])):
        if a.get('shop_key') not in shops: err(f'social[{i}]: unresolved shop')
        if a.get('identity_status')=='verified' and not a.get('identity_evidence_source_ids'): err(f'social[{i}]: verified association lacks evidence')
        if a.get('access_status')=='private_excluded': err(f'social[{i}]: private profile must not be in delivered account list')
        for sid in a.get('identity_evidence_source_ids',[]):
            if sid not in sources: err(f'social[{i}]: unresolved source')
    inv=inventory_report(b)
    errors.extend('inventory: '+x for x in inv['errors'])
    minimum=run.get('min_qualified_shops'); qualified=sum(q.get('status')=='well_supported' for q in qualifications.values())
    if minimum is not None and (not isinstance(minimum,int) or isinstance(minimum,bool) or minimum<0): err('Invalid minimum qualified shops')
    elif minimum is not None and qualified<minimum: warnings.append(f'Qualified {qualified} below requested minimum {minimum}; report partial, do not pad.')
    qa=b.get('qa',{})
    if run.get('stage')=='delivery':
        if qa.get('semantic_status')!='passed' or not isinstance(qa.get('extractor'),str) or not qa.get('extractor','').strip() or not isinstance(qa.get('independent_reviewer'),str) or not qa.get('independent_reviewer','').strip() or qa.get('independent_reviewer')==qa.get('extractor'): err('Delivery requires an independent semantic audit or must remain partial/draft')
        if not nonblank(qa.get('semantic_audit_ref')) or not qa.get('audited_categories') or any(not nonblank(v) for v in qa.get('audited_categories',[])): err('Delivery requires nonempty string semantic audit reference and audited categories')
        if qa.get('source_integrity_status')!='passed': err('Delivery requires passed source integrity audit')
        checks=qa.get('output_checks',[])
        if not checks or any(not isinstance(x,dict) or x.get('passed') is not True or not nonblank(x.get('artifact')) or not nonblank(x.get('check')) for x in checks): err('Delivery requires explicit successful output checks and artifact references')
        if run.get('inventory_stop')!='not_requested' and not inv.get('complete'): err('Delivery stage requires reconciled requested inventory; use draft/partial for incomplete scope')
        if not sources or not listings: err('Empty research is not a completed delivery')
        for cat,n in qa.get('errors_by_category',{}).items():
            if n and (cat not in qa.get('expanded_categories',[]) or qa.get('category_audit_complete',{}).get(cat) is not True): err(f'Category {cat}: errors require completed full affected-category audit')
    return {'passed':not errors,'errors':errors,'warnings':warnings,'qualified_shops':qualified,'requested_goal_met': None if minimum is None else qualified>=minimum if isinstance(minimum,int) and not isinstance(minimum,bool) else False,'inventory':inv,'limitations':LIMITS}

def main():
    ap=argparse.ArgumentParser(description=__doc__); sp=ap.add_subparsers(dest='command',required=True)
    age=sp.add_parser('age'); age.add_argument('text')
    for command in ['inventory','validate']:
        p=sp.add_parser(command); p.add_argument('bundle'); p.add_argument('--source-root')
    a=ap.parse_args()
    try:
        if a.command=='age': result=parse_age(a.text); code=0 if result['status']=='display_duration' else 1
        else:
            b=json.loads(Path(a.bundle).read_text(encoding='utf-8'))
            if not isinstance(b,dict): raise ValueError('Bundle must be a JSON object')
            result=inventory_report(b) if a.command=='inventory' else validate(b,a.source_root)
            code=1 if result.get('errors') else 0
        print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)); return code
    except (OSError,ValueError,TypeError,KeyError,AttributeError) as e:
        print(json.dumps({'error':str(e),'status':'invalid_input'},ensure_ascii=False)); return 2
if __name__=='__main__': sys.exit(main())
