#!/usr/bin/env python3
"""Read-only CSV ingestion; audited keyword cleaning. Python 3 + optional xlsxwriter."""
import argparse,csv,datetime as dt,json,re,sqlite3,sys,unicodedata,os
from pathlib import Path
P={'unknown','n/a','na','n.a.','none','null','undefined','unavailable','not available','no data','no results','test','sample','-1','?','--'}
ALIASES={'searches':['Average Searches USA','Average Searches','Avg Searches','Searches','Volume','Avg Search Volume','Average Searches (USA)'],'clicks':['Average Clicks USA','Average Clicks','Avg Clicks','Avg Clicks USA','Clicks','Average Clicks (USA)'],'ctr':['Average CTR USA','Average CTR','Avg CTR','CTR','Average CTR (USA)'],'competition':['Etsy Competition','Etsy Competition USA','Competition','Etsy Competition (USA)'],'difficulty':['Keyword Difficulty','Keyword Difficulty USA','KD','Keyword Difficulty (USA)'],'tag_occurrences':['Tag Occurrences'],'character_count':['Character Count'],'google_searches':['Google Searches','Google Searches USA'],'keyword_score':['Keyword Score'],'long_tail':['Long Tail Keywords'],'serp_analysis':['SERP Analysis']}
RULES=[('Faith & Religious',r'\b(?:baptis\w*|christen\w*|communion|confirmation|christian|church|bible|faith|prayer|pastor|priest|god|scripture|cross|religious|spiritual)\b'),('Wedding & Anniversary',r'\b(?:wedding|bride|bridal|groom|marriage|anniversary|vow|engagement)\b'),('Birthday & Milestones',r'\b(?:birthday|bday|\d+(?:st|nd|rd|th)|graduat\w*|retirement|retire|promotion|new baby|baby shower)\b'),('Seasonal & Holidays',r"\b(?:christmas|xmas|halloween|thanksgiving|valentine|easter|mother.?s day|father.?s day|holiday|ornament)\b"),('Memorial & Remembrance',r'\b(?:memorial|remembrance|in memory|sympathy|funeral|loss of|condolence)\b'),('Family & Relationships',r'\b(?:mom|mother|mum|dad|father|grandma|grandmother|grandpa|grandfather|daughter|son|sister|brother|wife|husband|couple|family|friend|teacher|coach|nurse|pastor)\b'),('Pet Gifts',r'\b(?:dog|cat|pet|puppy|kitten)\b'),('Journal & Stationery',r'\b(?:journal|notebook|diary|planner|writing|book|stationery)\b'),('Personalized Gifts',r'\b(?:personalized|personalised|custom|customized|customised|name gift)\b'),('Gift Ideas',r'\b(?:gift|gifts|present|keepsake)\b')]
LIBS=['Occasions, Faith & Holidays','Recipients & Relationships','Products & Personalization','Gifts & Keepsakes','Needs Review (TBC)']
NAMES=['Occasions_Faith_Holidays','Recipients_Relationships','Products_Personalization','Gifts_Keepsakes','Needs_Review_TBC']
def h(s):return re.sub('[^a-z0-9]+',' ',s.lstrip('\ufeff').lower()).strip()
def normalize(s):return re.sub(r'\s+',' ',s.strip().lower())
def metric(s):
 s=s.strip()
 if not s or s.casefold() in P:return {'raw':s,'value':None,'status':'missing'}
 if re.fullmatch(r'[<>]=?\s*[+-]?[\d,]+(?:\.\d+)?%?',s):return {'raw':s,'value':None,'status':'threshold'}
 if re.fullmatch(r'[+-]?(?:\d[\d,]*(?:\.\d+)?|\.\d+)%?',s):
  n=float(s.replace(',','').replace('%',''));return {'raw':s,'value':int(n) if n.is_integer() else n,'status':'observed' if n>=0 else 'missing'}
 return {'raw':s,'value':None,'status':'unparsed'}
def category(k):
 tags=[name for name,pattern in RULES if re.search(pattern,k,re.I)];specific=tags[0] if tags else 'Unclassified (TBC)'
 if specific in [x[0] for x in RULES[:5]]:lib=LIBS[0]
 elif specific in [x[0] for x in RULES[5:7]]:lib=LIBS[1]
 elif specific in [x[0] for x in RULES[7:9]]:lib=LIBS[2]
 elif specific=='Gift Ideas':lib=LIBS[3]
 else:lib=LIBS[4]
 return lib,specific,tags

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-dir',required=True);ap.add_argument('--output-dir',required=True);ap.add_argument('--scope-json',required=True);ap.add_argument('--date-policy',required=True,choices=['effective-latest','explicit-first']);ap.add_argument('--unknown-policy',choices=['exclude','retain-review'],default='exclude');ap.add_argument('--english-only',action='store_true');ap.add_argument('--xlsx',action='store_true');a=ap.parse_args()
 src=Path(a.input_dir).resolve();out=Path(a.output_dir).resolve()
 if not src.is_dir():ap.error('input directory missing')
 if out==src or src in out.parents:ap.error('output must be outside the source tree')
 if out.exists():ap.error('output must be a NEW directory; never overwrite a prior run')
 scopes=json.loads(Path(a.scope_json).read_text(encoding="utf-8"));default=scopes.get('default',{});overrides=scopes.get('files',{})
 out.mkdir(parents=True);db=sqlite3.connect(out/'audit.sqlite');db.execute('create table rows (id integer primary key, dedupe_key text, priority integer, effective text, modified text, quality integer, body text)')
 manifest={'version':'1.0-safe','settings':vars(a),'sources':[],'counts':{'input_rows':0,'selected':0,'duplicates':0,'rejected':0,'review':0},'quality_changes':['Strict decoding; schema/header failures registered','Dedup key includes platform/country/language/metric_period','Corrected word-boundary classifier; taxonomy remains heuristic','Explicit unknown date/timezone handling','No older-volume backfill; unparsed volume requires review','Corrected populated-field quality; unresolved equal-rank disagreements require review'],'coverage_complete':True}
 manifest['selected_search_status_counts']={};manifest['selected_category_counts']={};rejected=[];rowid=0
 for p in sorted(src.glob('*.csv')):
  file_label=os.fsencode(p.name).decode('utf-8',errors='replace')
  scope={**default,**overrides.get(file_label,{})};meta={'file':file_label,'path':str(p),'rows':0,'status':'pending','error':None};manifest['sources'].append(meta)
  required=['platform','country','language','metric_period','source_tool','metric_definition']
  if any(not isinstance(scope.get(k),str) or not scope[k].strip() or scope[k].strip().casefold() in P for k in required):meta.update(status='blocked_scope',error='Supply verified platform, country, language, metric_period, source_tool, metric_definition');manifest['coverage_complete']=False;continue
  if scope['platform'].casefold()!='etsy':meta.update(status='blocked_platform',error='This helper accepts Etsy keyword exports only');manifest['coverage_complete']=False;continue
  stamp=dt.datetime.fromtimestamp(p.stat().st_mtime,dt.timezone.utc).isoformat(timespec='seconds');filedate=''
  m=re.search(r'20\d{6}',file_label)
  if m:
   try:filedate=dt.datetime.strptime(m[0],'%Y%m%d').date().isoformat()
   except ValueError:meta['date_warning']='Invalid filename date'
  explicit=scope.get('explicit_export_date',filedate)
  if explicit:
   try:explicit=dt.date.fromisoformat(explicit).isoformat()
   except ValueError:meta.update(status='blocked_date',error='Invalid explicit export date');manifest['coverage_complete']=False;continue
  effective=explicit or stamp[:10];meta.update(scope=scope,modified_utc=stamp,explicit_date=explicit,used_date=effective,date_basis='Explicit export/filename date' if explicit else 'File modified date (UTC proxy)')
  try:
   with p.open(encoding=scope.get('encoding','utf-8-sig'),errors='strict',newline='') as f:
    sample=f.read(5000);f.seek(0)
    try:dialect=csv.Sniffer().sniff(sample,delimiters=',\t;')
    except csv.Error:dialect=csv.excel;meta['delimiter_warning']='Sniffer failed; comma CSV fallback'
    reader=csv.DictReader(f,dialect=dialect);headers=reader.fieldnames or [];norm={h(x):x for x in headers if x};meta['headers']=headers
    if len(norm)!=len(headers):raise ValueError('Blank or colliding normalized headers')
    kw=next((norm[k] for k in ['keyword','keywords','tag'] if k in norm),None)
    is_us=scope['country'].casefold() in {'us','usa','united states'}
    cols={}
    for canonical,values in ALIASES.items():
     found=list(dict.fromkeys(norm[h(x)] for x in values if h(x) in norm and (is_us or 'usa' not in h(x).split())))
     if len(found)>1 and canonical not in scope.get('field_map',{}):raise ValueError('Ambiguous metric headers for '+canonical+'; supply field_map')
     cols[canonical]=found[0] if found else None
    for canonical,actual in scope.get('field_map',{}).items():
     if canonical not in ALIASES or actual not in headers:raise ValueError('Invalid explicit field mapping')
     cols[canonical]=actual
    if not is_us and any(c and re.search(r'\b(?:usa|united states)\b',h(c)) for c in cols.values()):raise ValueError('USA-labelled metric header conflicts with non-US scope')
    if not kw or not any(cols[k] for k in ['searches','competition','difficulty','keyword_score']):raise ValueError('Not a supported keyword-export schema')
    if not cols['searches']:raise ValueError('Search-volume column unavailable; map before active-library cleaning')
    meta['column_map']={'keyword':kw,**cols}
    for number,r in enumerate(reader,2):
     meta['rows']+=1;manifest['counts']['input_rows']+=1;rowid+=1
     if None in r or any(v is None for v in r.values()):
      rejected.append({'row_id':rowid,'source_file':file_label,'source_row':number,'source_row_basis':'CSV logical record including header','raw_fields':r,'disposition':'rejected','reason':'Malformed CSV record: extra or missing fields'});manifest['counts']['rejected']+=1
      raise ValueError(f'Malformed CSV fields at data row {number}; preserved in audit; unread remainder unknown')
     raw=r.get(kw) or '';key=normalize(raw);metrics={k:metric(r.get(c) or '') if c and k not in ['long_tail','serp_analysis'] else {'raw':r.get(c) or '' if c else '', 'value':None,'status':'text'} for k,c in cols.items()}
     lib,specific,tags=category(key);body={'row_id':rowid,'keyword_raw':raw,'keyword_normalized':key,'scope':scope,'source_file':file_label,'source_row':number,'source_row_basis':'CSV logical record including header','source_modified_utc':stamp,'observation_date':effective,'date_basis':meta['date_basis'],'metrics':metrics,'raw_fields':r,'library':lib,'specific_category':specific,'theme_tags':tags,'classification_confidence':'rule-based; owner review'}
     noise=not key or key.casefold() in P or not any(ch.isalpha() for ch in key) or (a.english_only and not re.search('[a-z]',key))
     if noise:body['disposition']='rejected';body['reason']='keyword placeholder/empty/no letters or explicit English-only filter';rejected.append(body);manifest['counts']['rejected']+=1;continue
     volume=metrics['searches'];valid=volume['status'] in ['observed','threshold'];quality=(100 if valid else 0)+sum(v['status'] in ['observed','threshold'] or (v['status']=='text' and bool(v['raw'].strip())) for v in metrics.values())
     group=json.dumps([scope[k] for k in required]+[key],ensure_ascii=True);priority=int(bool(explicit)) if a.date_policy=='explicit-first' else 0
     db.execute('insert into rows values (?,?,?,?,?,?,?)',(rowid,group,priority,effective,stamp,quality,json.dumps(body,ensure_ascii=True)))
   meta['status']='processed'
  except Exception as e:meta.update(status='error',error=str(e),unread_remainder='unknown');manifest['coverage_complete']=False
 db.commit()
 # Never silently deliver a partial file as a complete successful run.
 audit=(out/'audit.ndjson').open('w',encoding='utf-8',newline='');selected=(out/'selected.ndjson').open('w',encoding='utf-8',newline='');review=(out/'review.ndjson').open('w',encoding='utf-8',newline='')
 def emit(f,r):f.write(json.dumps(r,ensure_ascii=True)+'\n')
 for r in rejected:emit(audit,r)
 current=None;winner=None;rank=None;group=[]
 def finish(group):
  if not group:return
  best=group[0];brank=best[1:6];body=json.loads(best[6]);ties=[x for x in group[1:] if x[1:6]==brank]
  conflict=any(json.loads(x[6])['metrics']!=body['metrics'] for x in ties)
  vol=body['metrics']['searches'];state='selected';reason='Latest comparable observation; no older backfill'
  if conflict:state='review';reason='Equal rank with conflicting metrics'
  elif vol['status']=='unparsed':state='review';reason='Unparsed search volume'
  elif vol['status']=='missing':state='review' if a.unknown_policy=='retain-review' else 'rejected';reason='Latest search volume missing; never backfill an older known value'
  body.update(disposition=state,reason=reason,all_source_occurrences=[{'file':json.loads(x[6])['source_file'],'row':json.loads(x[6])['source_row']} for x in group]);manifest['counts'][state]+=1;emit(audit,body)
  if state=='selected':
   emit(selected,body)
   token='observed_zero' if vol['status']=='observed' and vol['value']==0 else vol['status'];manifest['selected_search_status_counts'][token]=manifest['selected_search_status_counts'].get(token,0)+1;manifest['selected_category_counts'][body['library']]=manifest['selected_category_counts'].get(body['library'],0)+1
  if state=='review':emit(review,body)
  for x in group[1:]:r=json.loads(x[6]);r.update(disposition='duplicates',reason='Superseded/comparable duplicate',selected_row_id=body['row_id']);manifest['counts']['duplicates']+=1;emit(audit,r)
 for row in db.execute('select id,dedupe_key,priority,effective,modified,quality,body from rows order by dedupe_key,priority desc,effective desc,modified desc,quality desc,id'):
  if current is not None and row[1]!=current:finish(group);group=[]
  current=row[1];group.append(row)
 finish(group);audit.close();selected.close();review.close();db.close()
 c=manifest['counts'];manifest['count_invariant']=c['input_rows']==sum(c[k] for k in ['selected','duplicates','rejected','review']);manifest['status']='COMPLETE' if manifest['coverage_complete'] and manifest['count_invariant'] and c['review']==0 else 'PARTIAL'
 if not manifest['sources'] or (c['input_rows']==0 and manifest['coverage_complete']):manifest['status']='EMPTY'
 elif not any(x['status']=='processed' for x in manifest['sources']):manifest['status']='BLOCKED'
 elif c['selected']==0 and c['review']==0 and manifest['coverage_complete']:manifest['status']='EMPTY'
 if a.xlsx and c['selected']>0:
  try:build_xlsx(out,manifest)
  except Exception as e:manifest['status']='PARTIAL';manifest['xlsx_error']=str(e)
 (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=True,indent=2),encoding='utf-8');print(json.dumps({'output':str(out),'status':manifest['status'],'counts':c},ensure_ascii=True))
 return 0 if manifest['status']=='COMPLETE' else 2

def build_xlsx(out,manifest):
 import xlsxwriter,zipfile,xml.etree.ElementTree as ET
 header=['Keyword','Search Volume','Competition','Keyword Difficulty','Average Clicks','CTR (source value)','Google Searches','Keyword Score','Specific Category','Related Theme Tags','Tag Occurrences','Character Count','Long Tail Keywords','SERP Analysis','Source Date','Source Date Basis','Source File','Source Row','File Modified At (UTC)','Platform','Country','Language','Metric Period','Source Tool','Metric Definition']
 stage=out/'workbooks';stage.mkdir();work={};counts={x:0 for x in LIBS};source_selected={x:{} for x in LIBS}
 for i,lib in enumerate(LIBS):
  path=stage/f'Keyword_Library_{i+1:02}_{NAMES[i]}.xlsx';wb=xlsxwriter.Workbook(path,{'constant_memory':True,'strings_to_formulas':False,'strings_to_urls':False});ws=wb.add_worksheet('Keywords');ws.write_row(0,0,header);ws.freeze_panes(1,1);ws.set_column(0,0,40);ws.set_column(1,len(header)-1,23);work[lib]=(wb,ws,path)
 with (out/'selected.ndjson').open(encoding='utf-8') as f:
  for line in f:
   r=json.loads(line);lib=r['library'];wb,ws,path=work[lib];m=r['metrics'];keys=['searches','competition','difficulty','clicks','ctr','google_searches','keyword_score'];values=[m[k]['value'] if m[k]['status']=='observed' else m[k]['raw'] for k in keys];row=[r['keyword_raw'],*values,r['specific_category'],'; '.join(r['theme_tags']),*[m[k]['value'] if m[k]['status']=='observed' else m[k]['raw'] for k in ['tag_occurrences','character_count','long_tail','serp_analysis']],r['observation_date'],r['date_basis'],r['source_file'],r['source_row'],r['source_modified_utc'],*[r['scope'][k] for k in ['platform','country','language','metric_period','source_tool','metric_definition']]];counts[lib]+=1;source_selected[lib][r['source_file']]=source_selected[lib].get(r['source_file'],0)+1;ws.write_row(counts[lib],0,row)
   for column,k in enumerate(keys,1):
    if m[k]['status']=='observed' and m[k]['raw'].endswith('%'):ws.write_number(counts[lib],column,m[k]['value'],wb.add_format({'num_format':'0.########"%"'}))
 for lib,(wb,ws,path) in work.items():
  ws.autofilter(0,0,max(1,counts[lib]),len(header)-1);ov=wb.add_worksheet('Overview');ov.write_row(0,0,['Measure','Value']);ov.write_row(1,0,['Selected keywords',counts[lib]]);ov.write_row(2,0,['Coverage status',manifest['status']]);ov.write_row(3,0,['Date policy',manifest['settings']['date_policy']]);ov.write_row(4,0,['Limit','Historical exports; not current trend verification']);ov.write_row(5,0,['Audit','See audit.ndjson and manifest.json for full source-row dispositions']);sf=wb.add_worksheet('Source Files');sf.write_row(0,0,['Source File','Global Input Rows Read','Status','Explicit Date','Modified UTC','Error','Selected In This Library']);
  for i,s in enumerate(manifest['sources'],1):sf.write_row(i,0,[s['file'],s['rows'],s['status'],s.get('explicit_date',''),s.get('modified_utc',''),s.get('error') or '',source_selected[lib].get(s['file'],0)])
  j=6
  for label,value in [('Global '+k,v) for k,v in manifest['counts'].items()]+[('Selected search '+k,v) for k,v in manifest['selected_search_status_counts'].items()]+[('Taxonomy','Rule-based five libraries; ambiguous terms need owner review'),('Scope','See per-row Platform/Country/Language/Metric Period/Source Tool/Metric Definition'),('Corrections','See manifest quality_changes'),('Dates','Proxy dates are not proof of observation recency')]:ov.write_row(j,0,[label,value]);j+=1
  sf.freeze_panes(1,0);sf.autofilter(0,0,max(1,len(manifest['sources'])),6);wb.close()
  with zipfile.ZipFile(path) as z:
   if z.testzip() is not None:raise ValueError('Corrupt workbook '+str(path))
   ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'};doc=ET.fromstring(z.read('xl/workbook.xml'));names=[x.attrib['name'] for x in doc.findall('m:sheets/m:sheet',ns)]
   if names!=['Keywords','Overview','Source Files']:raise ValueError('Sheet order mismatch')
   data=ET.fromstring(z.read('xl/worksheets/sheet1.xml'));rows=data.findall('m:sheetData/m:row',ns)
   if len(rows)!=counts[lib]+1 or data.find('m:autoFilter',ns) is None or data.find('m:sheetViews/m:sheetView/m:pane',ns) is None:raise ValueError('Workbook structure mismatch')
 manifest['workbooks']={lib:{'file':str(work[lib][2]),'rows':counts[lib]} for lib in LIBS}
if __name__=='__main__':sys.exit(main())
