#!/usr/bin/env python3
"""Check a lightweight semantic-review record. Does not certify human judgments."""
import argparse, hashlib, json, pathlib, re, sys
ROLES={'A','B','C','D','E'}
VOLUME={'number','zero','threshold','unknown','missing','unavailable','not_queried','related_only'}
def norm(s): return ' '.join(s.casefold().split())
def check(p, base=None):
    errors=[]
    def need(ok,msg):
        if not ok: errors.append(msg)
    need(p.get('schema')=='coach-assurance/1','schema must be coach-assurance/1')
    need(p.get('scope') in {'draft','keyword_release'},'scope missing/invalid')
    need(p.get('identity')=='source_based_ai_review','must identify source-based AI review')
    need(not p.get('claims_live_coach_participation',False),'no invented live coach participation')
    need(not p.get('claims_market_success',False),'review is not market proof')
    artifact=p.get('artifact',{})
    need(bool(artifact.get('version')),'artifact version missing')
    sha=artifact.get('sha256','')
    need(bool(re.fullmatch('[0-9a-f]{64}',sha)),'artifact sha256 missing/invalid')
    if base is not None and not p.get('synthetic',False):
        path=base/artifact.get('path','')
        need(path.is_file(),'artifact file unavailable')
        if path.is_file(): need(hashlib.sha256(path.read_bytes()).hexdigest()==sha,'artifact hash mismatch')
    selected=artifact.get('selected_tags',[])
    need(bool(selected),'selected tags missing')
    need(len(set(map(norm,selected)))==len(selected),'duplicate selected tags')
    terms=p.get('term_reviews',[])
    names=[norm(t.get('phrase','')) for t in terms]
    need(len(set(names))==len(names),'duplicate phrase review')
    need(set(map(norm,selected)).issubset(names),'every actual tag needs its own review')
    for t in terms:
        name=t.get('phrase',''); pre=name+': '
        need(bool(name), 'blank phrase')
        need(t.get('fit') in {'truthful','conditional','mismatch'},pre+'fit missing')
        need(t.get('intent') in {'specific','broad','ambiguous'},pre+'intent missing')
        need(t.get('evidence') in {'qualified_estimate','limited','unknown','stale','invalid'},pre+'evidence missing')
        need(t.get('decision') in {'core_identity','demand_supported_test','bounded_test','description','hold','reject'},pre+'decision missing')
        v=t.get('volume_state');need(v in VOLUME,pre+'volume state missing/invalid')
        need(bool(t.get('evidence_refs')),pre+'evidence record/hypothesis reference missing')
        need(bool(t.get('reason')),pre+'decision reason missing')
        need(t.get('market') in {'verified_US','verified_other','unverified','not_applicable'},pre+'market state missing')
        if t.get('fit')=='mismatch':need(t.get('decision') in {'reject','hold'},pre+'product mismatch cannot be selected')
        if norm(name) in set(map(norm,selected)):
            need(t.get('decision') not in {'reject','hold','description'},pre+'active tag conflicts with allocation')
        if t.get('evidence') in {'unknown','stale','invalid'} or v in {'unknown','missing','unavailable','not_queried','related_only'}:
            need(t.get('decision')!='demand_supported_test',pre+'uncertain/invalid evidence cannot be measured-demand test')
        if t.get('numeric_claim_for_phrase'):
            need(v in {'number','zero','threshold'} and t.get('exact_phrase_join') is True,pre+'numeric claim needs exact qualified phrase join')
            need(bool(t.get('measurement_mode')) and bool(t.get('period')),pre+'numeric claim needs actual measurement mode/window')
        if t.get('claims_current_US_demand'):
            need(t.get('market')=='verified_US' and t.get('evidence')=='qualified_estimate',pre+'current US demand requires qualified US evidence')
        if t.get('claims_trend'):
            need(t.get('trend_basis')=='multiple_comparable_periods',pre+'single month/average cannot establish trend')
        risks=set(t.get('risks',[]))
        derived=set()
        if v in {'unknown','missing','unavailable','not_queried','related_only'}:derived.add('unquantified')
        if v in {'zero','threshold'}:derived.add('limited_volume')
        if t.get('market')=='unverified':derived.add('scope_unknown')
        if t.get('evidence')=='stale':derived.add('stale')
        if t.get('intent') in {'broad','ambiguous'}:derived.add('intent_uncertain')
        need(derived.issubset(risks),pre+'derived risk flags omitted: '+','.join(sorted(derived-risks)))
        if risks:
            need(bool(t.get('risk_disposition')) and bool(t.get('change_evidence')),pre+'risk needs disposition and change-evidence')
        need(not t.get('volume_only_decision',False),pre+'volume-only decision is prohibited')
        need(not t.get('tags_prove_traffic',False),pre+'actual tags do not prove traffic')
    available={(norm(e.get('phrase','')),e.get('field')) for e in p.get('available_evidence',[]) if e.get('source_refs')}
    for q in p.get('new_queries',[]):
        need(all(q.get(k) for k in ['phrase','vault_version_checked','existing_source_ids_checked','unresolved_field','why_existing_insufficient','decision_changed','stop_condition','unresolved_field_key']),'new query lacks reuse/gap/decision/stop justification')
        need({'terms','observations','monthlyEvidence','raw_source_index'}.issubset(q.get('source_sections_checked',[])),'new query lacks full source-section search, including monthlyEvidence')
        need((norm(q.get('phrase','')),q.get('unresolved_field_key')) not in available or q.get('request_kind')=='revalidation','existing field cannot be requested as missing; justify revalidation separately')
    reviews=p.get('reviews',[]); coverage=set();families=set();fresh_independent=False
    run_ids=[r.get('run_id') for r in reviews]
    need(len(set(run_ids))==len(run_ids),'duplicate run_id cannot create independence')
    for r in reviews:
        roles=set(r.get('roles',[]));coverage.update(roles);families.update(r.get('source_families',[]))
        need(bool(roles) and roles.issubset(ROLES),'review needs nonempty valid decision-role scope')
        outcomes=r.get('role_outcomes',{})
        need(set(outcomes)==roles and all(v in {'PASS','REVISE','BLOCKED'} for v in outcomes.values()),'role outcomes must cover exactly the reviewed roles')
        if r.get('outcome')=='PASS':need(bool(outcomes) and all(v=='PASS' for v in outcomes.values()),'overall PASS cannot hide non-PASS role finding')
        need(bool(r.get('run_id')) and bool(r.get('source_refs_opened')), 'review needs actual run/source record')
        need(r.get('outcome') in {'PASS','REVISE','BLOCKED'},'review outcome invalid')
        if r.get('independent'):
            need(r.get('author_participation') is False and r.get('preloaded_consensus') is False,'independence cannot be author/self-review or consensus-preloaded')
            fresh_independent |= r.get('author_participation') is False and r.get('preloaded_consensus') is False
    if p.get('scope')=='keyword_release':
        need(ROLES.issubset(coverage),'release lacks decision-role coverage A–E')
        need(len(families)>=3,'release requires three distinct method/source families')
        need(fresh_independent,'release requires a fresh independent outcome review')
        need(bool(reviews) and all(r.get('outcome')=='PASS' for r in reviews),'open reviewer finding blocks release')
        gate=p.get('base_evidence_gate',{})
        need(isinstance(gate,dict) and gate.get('status')=='PASS' and gate.get('artifact_version')==artifact.get('version') and gate.get('artifact_sha256')==sha and bool(gate.get('evidence_ref')),'original evidence-release gate must separately pass with matching artifact version/hash and report')
        need(p.get('unresolved_conflicts')==[],'unresolved conflicts block complete release')
    return errors

def main():
    ap=argparse.ArgumentParser();ap.add_argument('packet');a=ap.parse_args()
    path=pathlib.Path(a.packet)
    try:
        p=json.loads(path.read_text());errors=check(p,path.parent)
    except (OSError,ValueError,TypeError,AttributeError,KeyError) as exc:
        errors=['invalid packet: '+str(exc)]
    print(json.dumps({'status':'REVISE' if errors else 'STRUCTURAL_PASS','errors':errors,'semantic_truth_verified':False,'market_success_verified':False},ensure_ascii=False,indent=2))
    return bool(errors)
if __name__=='__main__':sys.exit(main())
