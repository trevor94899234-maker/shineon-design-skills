"""Small, offline regressions grounded in actual research failure classes."""
import copy
import hashlib
import importlib.util
import json
import tempfile
import subprocess
import sys
import unittest
from pathlib import Path

MODULE=Path(__file__).resolve().parents[1]/'scripts'/'research_checks.py'
spec=importlib.util.spec_from_file_location('checks',MODULE); checks=importlib.util.module_from_spec(spec); spec.loader.exec_module(checks)
TIME='2026-10-05T18:00:00+00:00'
RAW='Vegan leather cover. Printed, not engraved. Optional engraved pen. To my daughter. Love, Mom and Dad.'

def fixture():
    return {'schema_version':'1.0','run':{'run_id':'fixture','mode':'research_only','stage':'draft','buyer_country':'US','currency':'USD','language':'en','collected_at':TIME,'target_decision':'Compare supported gifts','min_qualified_shops':None,'inventory_expected':None,'inventory_stop':'not_requested','inventory_snapshot_id':None},
    'sources':[{'source_id':'S1','source_url':'https://www.etsy.com/listing/123','captured_at':TIME,'method':'fixture Etsy detail observation','market_scope':'US buyer context; not US demand','raw_file':'raw.txt','sha256':hashlib.sha256(RAW.encode()).hexdigest(),'text':{'description':RAW,'age':'1.5 years on Etsy'}}],
    'shops':[{'shop_key':'etsy:shop:10','shop_id':'10','shop_name':'FixturePrints','source_id':'S1','age_raw':'1.5 years on Etsy','age_years':1.5,'observed_at':TIME}],
    'listings':[{'listing_key':'etsy:listing:123','listing_id':'123','shop_key':'etsy:shop:10','source_id':'S1','observed_at':TIME,'title':'Fixture journal','description':RAW,'tags':['daughter journal'],'tags_provenance':'actual connected listing details','selected':True,'detail_captured':True,'comparator_class':'direct','price_raw':None,'price':None,'currency':None,'variant':None,'quantity':None,'shipping_raw':None,'shipping_cost':None,'shipping_scope':None}],
    'metrics':[],'claims':[],'inventory_pages':[],'qualifications':[],'keywords':[],'corrections':[],'social_accounts':[],
    'qa':{'extractor':'extractor','independent_reviewer':None,'semantic_status':'pending','errors_by_category':{},'expanded_categories':[],'category_audit_complete':{},'semantic_audit_ref':'fixture-audit','audited_categories':['roles','materials','metrics'],'source_integrity_status':'passed','output_checks':[{'artifact':'fixture','check':'structure','passed':True}]}}

def claim():
    return {'claim_id':'C1','entity_key':'etsy:listing:123','claim_type':'process','value':'Printed (seller stated)','status':'supported','source_id':'S1','source_field':'description','quote':'Printed, not engraved.','polarity':'positive','target':'cover','reviewer':'reader','reviewed_at':TIME}

def metric():
    return {'metric_id':'M1','entity_key':'etsy:shop:10','metric':'shop_sales_cumulative','source_id':'S1','raw_value':'123','value':123,'status':'observed','qualifier':'exact','entity_scope':'shop','period':'lifetime','market_scope':'all markets','definition':'Shop cumulative all-product transactions','caveat':'Not listing sales or profit'}

class AgeTests(unittest.TestCase):
    def test_decimal_not_trailing_integer(self):
        for raw,years in [('1.5 years on Etsy',1.5),('2.5 years\n\non Etsy',2.5),('9 months on Etsy',.75),('1 year 6 months on Etsy',1.5),('1.5y',1.5),('18 mo',1.5),('.5 years',.5)]:
            with self.subTest(raw=raw): self.assertEqual(checks.parse_age(raw)['years'],years)
    def test_ambiguous_not_guessed(self):
        for raw in ['1-5 years','1.5 or 2.5 years','1.5.5 years','About 2 years','Since 2020','5 year birthday gift','-1.5 years','1 year 13 months','0.5 years 9 months and 2 years']:
            with self.subTest(raw=raw): self.assertIsNone(checks.parse_age(raw)['years'])
    def test_unknown(self): self.assertEqual(checks.parse_age(None)['status'],'missing')

class GuardrailTests(unittest.TestCase):
    def test_valid_draft(self): self.assertTrue(checks.validate(fixture())['passed'])
    def test_ids_from_actual_etsy_url(self):
        self.assertEqual(checks.canonical_listing('https://www.etsy.com/listing/123/a-title?ref=ad'),'etsy:listing:123')
        self.assertEqual(checks.canonical_listing('https://www.etsy.com/uk/listing/123/a-title'),'etsy:listing:123')
        self.assertIsNone(checks.canonical_listing('https://etsy.com.evil.invalid/listing/123'))
        self.assertIsNone(checks.canonical_listing('https://www.etsy.com/shop/Name'))
    def test_id_mismatch(self):
        b=fixture(); b['listings'][0]['listing_id']='124'; self.assertFalse(checks.validate(b)['passed'])
    def test_age_regression(self):
        b=fixture(); b['shops'][0]['age_years']=5; self.assertFalse(checks.validate(b)['passed'])
    def test_months(self):
        b=fixture(); b['shops'][0].update(age_raw='9 months on Etsy',age_years=.75); self.assertTrue(checks.validate(b)['passed'])
    def test_missing_not_zero(self):
        b=fixture(); m=metric(); m.update(status='missing',value=0,raw_value=None); b['metrics']=[m]; self.assertFalse(checks.validate(b)['passed'])
    def test_displayed_zero_unavailable(self):
        b=fixture(); m=metric(); m.update(status='unavailable',value=None,raw_value=0,caveat='Analytics unavailable'); b['metrics']=[m]; self.assertTrue(checks.validate(b)['passed'])
    def test_less_than(self):
        b=fixture(); m=metric(); m.update(raw_value='<20',value=20); b['metrics']=[m]; self.assertFalse(checks.validate(b)['passed']); m['qualifier']='less_than'; self.assertTrue(checks.validate(b)['passed'])
    def test_shop_cumulative_scope(self):
        b=fixture(); m=metric(); m.update(entity_scope='listing',period='monthly'); b['metrics']=[m]; self.assertFalse(checks.validate(b)['passed'])
    def test_estimate_stays_estimate(self):
        b=fixture(); b['sources'][0]['method']='eRank native export'; b['metrics']=[metric()]; self.assertFalse(checks.validate(b)['passed']); b['metrics'][0]['status']='estimated'; self.assertTrue(checks.validate(b)['passed'])
    def test_actual_tag_does_not_prove_demand(self):
        b=fixture(); b['metrics']=[metric()]; b['keywords']=[{'keyword_id':'K1','phrase':'daughter journal','provenance':'actual_listing_tag','metric_ids':['M1'],'source_ids':['S1']}]; self.assertFalse(checks.validate(b)['passed'])
    def test_quote_exactness(self):
        b=fixture(); b['claims']=[claim()]; self.assertTrue(checks.validate(b)['passed']); b['claims'][0]['quote']='This cover is engraved'; self.assertFalse(checks.validate(b)['passed'])
    def test_negation_is_flagged_not_classified(self):
        flags=checks.risk_flags('Printed, not engraved.'); self.assertIn('negation',flags); self.assertIsInstance(flags,list)
    def test_quoted_negation_requires_reading(self):
        flags=checks.risk_flags('The phrase “not engraved” is printed inside.'); self.assertIn('negation',flags); self.assertIn('quoted_language',flags)
    def test_accessory_not_cover(self):
        flags=checks.risk_flags('Optional engraved pen included.'); self.assertIn('option_or_conditional',flags); self.assertIn('multiple_product_targets',flags)
    def test_shop_name_not_process(self):
        b=fixture(); b['claims']=[claim()]; b['claims'][0].update(quote='FixturePrints',source_field='shop_name'); self.assertFalse(checks.validate(b)['passed'])
    def test_grief_role_risk(self): self.assertIn('grief_or_deceased',checks.risk_flags('In memory of Dad, a journal for his grieving daughter.'))
    def test_multiple_roles_are_retained(self):
        b=fixture(); c=claim(); c.update(claim_type='recipient',quote='To my daughter.',value='daughter',target='gift recipient'); d=copy.deepcopy(c); d.update(claim_id='C2',claim_type='sender',quote='Love, Mom and Dad.',value='Mom and Dad',target='sender'); b['claims']=[c,d]; self.assertTrue(checks.validate(b)['passed']); self.assertEqual(len(b['claims']),2)
    def test_false_visual_evidence(self):
        b=fixture(); b['listings'][0].update(visual_inspected=True,visual_verified=False,visual_evidence={'visualVerified':False}); self.assertFalse(checks.validate(b)['passed'])
    def test_source_bytes(self):
        b=fixture()
        with tempfile.TemporaryDirectory() as p:
            Path(p,'raw.txt').write_text(RAW); self.assertTrue(checks.validate(b,p)['passed']); Path(p,'raw.txt').write_text('changed'); self.assertFalse(checks.validate(b,p)['passed'])
    def test_source_root_escape(self):
        b=fixture(); b['sources'][0]['raw_file']='../private.txt'
        with tempfile.TemporaryDirectory() as p: self.assertFalse(checks.validate(b,p)['passed'])
    def test_no_false_qualification_from_candidate_count(self):
        b=fixture(); b['run']['min_qualified_shops']=20; b['run']['candidate_goal']=50; r=checks.validate(b); self.assertEqual(r['qualified_shops'],0); self.assertTrue(any('below requested' in x for x in r['warnings']))
    def test_qualification_needs_evidence(self):
        b=fixture(); b['qualifications']=[{'shop_key':'etsy:shop:10','status':'well_supported'}]; self.assertFalse(checks.validate(b)['passed'])
    def test_independent_delivery_audit(self):
        b=fixture(); b['run']['stage']='delivery'; self.assertFalse(checks.validate(b)['passed']); b['qa'].update(semantic_status='passed',independent_reviewer='extractor'); self.assertFalse(checks.validate(b)['passed']); b['qa']['independent_reviewer']='other'; self.assertTrue(checks.validate(b)['passed'])
    def test_error_expands_entire_category(self):
        b=fixture(); b['run']['stage']='delivery'; b['qa'].update(semantic_status='passed',independent_reviewer='other',errors_by_category={'materials':1}); self.assertFalse(checks.validate(b)['passed']); b['qa'].update(expanded_categories=['materials'],category_audit_complete={'materials':True}); self.assertTrue(checks.validate(b)['passed'])
    def test_social_identity_proof(self):
        b=fixture(); b['social_accounts']=[{'shop_key':'etsy:shop:10','identity_status':'verified','identity_evidence_source_ids':[]}]; self.assertFalse(checks.validate(b)['passed']); b['social_accounts'][0]['identity_evidence_source_ids']=['S1']; self.assertTrue(checks.validate(b)['passed'])
    def test_private_social_excluded(self):
        b=fixture(); b['social_accounts']=[{'shop_key':'etsy:shop:10','identity_status':'unverified','access_status':'private_excluded'}]; self.assertFalse(checks.validate(b)['passed'])

class InventoryTests(unittest.TestCase):
    def inventory(self):
        b=fixture(); b['run'].update(inventory_expected=77,inventory_stop='verified_end',inventory_snapshot_id='live')
        b['inventory_pages']=[{'snapshot_id':'live','page_key':str(n),'previous_page_key':str(n-1) if n else None,'listing_ids':[str(i) for i in ids],'displayed_count':77,'observed_at':TIME,'source_id':'S1'} for n,ids in enumerate([range(1,37),range(37,73),range(73,78)])]; return b
    def test_36_36_5(self):
        r=checks.inventory_report(self.inventory()); self.assertTrue(r['complete']); self.assertEqual(r['unique_listing_count'],77)
    def test_cached126_fresh77_not_reconciled(self):
        b=self.inventory(); b['run']['inventory_expected']=126; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_featured_duplicates_removed(self):
        b=self.inventory(); b['inventory_pages'][1]['listing_ids'].append('1'); r=checks.inventory_report(b); self.assertTrue(r['complete']); self.assertEqual(r['duplicate_cards'],1)
    def test_partial_firstpage_not_complete(self):
        b=self.inventory(); b['inventory_pages']=b['inventory_pages'][:1]; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_missing_termination(self):
        b=self.inventory(); b['run']['inventory_stop']='partial'; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_repeated_cursor(self):
        b=self.inventory(); b['inventory_pages'][1]['page_key']='0'; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_repeated_content(self):
        b=self.inventory(); b['inventory_pages'][1]['listing_ids']=b['inventory_pages'][0]['listing_ids']; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_snapshot_drift(self):
        b=self.inventory(); b['inventory_pages'][2]['snapshot_id']='changed'; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_broken_page_chain(self):
        b=self.inventory(); b['inventory_pages'][2]['previous_page_key']='0'; self.assertFalse(checks.inventory_report(b)['complete'])


class IndependentReviewRegressions(unittest.TestCase):
    def test_snapshot_is_required(self):
        b=InventoryTests().inventory(); b['run']['inventory_snapshot_id']=None
        for p in b['inventory_pages']: p['snapshot_id']=None
        self.assertFalse(checks.inventory_report(b)['complete'])
    def test_inventory_source_join(self):
        b=InventoryTests().inventory(); b['inventory_pages'][0]['source_id']='GHOST'; self.assertFalse(checks.inventory_report(b)['complete'])
    def test_displayed_count_required(self):
        b=InventoryTests().inventory()
        for p in b['inventory_pages']: p['displayed_count']=None
        self.assertFalse(checks.inventory_report(b)['complete'])
    def test_bad_displayed_count(self):
        for value in ['77',True,-1,{}]:
            b=InventoryTests().inventory(); b['inventory_pages'][0]['displayed_count']=value
            with self.subTest(value=value): self.assertFalse(checks.inventory_report(b)['complete'])
    def test_shop_metric_cannot_point_at_listing(self):
        b=fixture(); m=metric(); m['entity_key']='etsy:listing:123'; b['metrics']=[m]; self.assertFalse(checks.validate(b)['passed'])
    def test_qualification_cannot_borrow_shop(self):
        b=fixture(); s=copy.deepcopy(b['shops'][0]); s.update(shop_key='etsy:shop:20',shop_id='20'); b['shops'].append(s)
        b['claims']=[claim()]; b['metrics']=[metric()]
        b['qualifications']=[{'shop_key':'etsy:shop:20','status':'well_supported','comparable_claim_ids':['C1'],'relevant_product_evidence_ids':['C1'],'success_metric_ids':['M1'],'rationale':'similar','caveats':['shop only'],'reviewed_at':TIME}]
        self.assertFalse(checks.validate(b)['passed'])
    def test_unknown_claim_cannot_have_ghost_source(self):
        b=fixture(); c=claim(); c.update(status='unknown',source_id='GHOST'); b['claims']=[c]; self.assertFalse(checks.validate(b)['passed'])
    def test_correction_entity_and_source_join(self):
        b=fixture(); b['corrections']=[{'correction_id':'R1','entity_key':'GHOST','source_ids':['GHOST']}]; self.assertFalse(checks.validate(b)['passed'])
    def test_shop_id_consistency(self):
        b=fixture(); b['shops'][0]['shop_id']='999'; self.assertFalse(checks.validate(b)['passed'])
    def test_detail_flag_must_be_boolean(self):
        b=fixture(); b['listings'][0]['detail_captured']='no'; self.assertFalse(checks.validate(b)['passed'])
    def test_listing_missing_field_is_explicit(self):
        b=fixture(); del b['listings'][0]['price_raw']; self.assertFalse(checks.validate(b)['passed'])
    def test_invalid_status(self):
        b=fixture(); m=metric(); m['status']='sure'; b['metrics']=[m]; self.assertFalse(checks.validate(b)['passed'])
    def test_string_false_not_completed_audit(self):
        b=fixture(); b['run']['stage']='delivery'; b['qa'].update(semantic_status='passed',independent_reviewer='other',errors_by_category={'materials':1},expanded_categories=['materials'],category_audit_complete={'materials':'false'}); self.assertFalse(checks.validate(b)['passed'])
    def test_failed_source_and_output_audits(self):
        for field,value in [('source_integrity_status','failed'),('output_checks',[{'artifact':'fixture','check':'open','passed':False}]),('extractor',None),('semantic_audit_ref',None),('audited_categories',[])]:
            b=fixture(); b['run']['stage']='delivery'; b['qa'].update(semantic_status='passed',independent_reviewer='other'); b['qa'][field]=value
            with self.subTest(field=field): self.assertFalse(checks.validate(b)['passed'])
    def test_no_negative_error_count(self):
        b=fixture(); b['qa']['errors_by_category']={'materials':-1}; self.assertFalse(checks.validate(b)['passed'])
    def test_partial_inventory_not_complete_delivery(self):
        b=InventoryTests().inventory(); b['run'].update(stage='delivery',inventory_stop='partial'); b['qa'].update(semantic_status='passed',independent_reviewer='other'); self.assertFalse(checks.validate(b)['passed'])
    def test_malformed_cli_returns_json_no_traceback(self):
        for field,value in [('run',[]),('qa',[]),('inventory_pages',['bad']),('sources',None)]:
            b=fixture(); b[field]=value
            with tempfile.TemporaryDirectory() as p:
                f=Path(p,'bundle.json'); f.write_text(json.dumps(b)); out=subprocess.run([sys.executable,str(MODULE),'validate',str(f)],capture_output=True,text=True)
                with self.subTest(field=field):
                    self.assertEqual(out.returncode,1); self.assertFalse(json.loads(out.stdout)['passed']); self.assertNotIn('Traceback',out.stderr)
    def test_nonstring_audit_evidence(self):
        b=fixture(); b['run']['stage']='delivery'; b['qa'].update(semantic_status='passed',independent_reviewer='other',semantic_audit_ref=True,audited_categories=[None],output_checks=[{'artifact':True,'check':True,'passed':True}]); self.assertFalse(checks.validate(b)['passed'])
    def test_listing_scalar_types(self):
        for field,value in [('title',{}),('description',[]),('price','nonsense'),('shipping_cost',True),('tags',[{}]),('quantity',0),('price',float('inf'))]:
            b=fixture(); b['listings'][0][field]=value
            with self.subTest(field=field): self.assertFalse(checks.validate(b)['passed'])
    def test_shop_identity_types(self):
        b=fixture(); b['shops'][0]['shop_id']=10; self.assertFalse(checks.validate(b)['passed']); b=fixture(); del b['shops'][0]['shop_name']; self.assertFalse(checks.validate(b)['passed'])
    def test_invalid_json_cli_exit2(self):
        with tempfile.TemporaryDirectory() as p:
            f=Path(p,'bad.json'); f.write_text('{bad'); out=subprocess.run([sys.executable,str(MODULE),'validate',str(f)],capture_output=True,text=True); self.assertEqual(out.returncode,2); self.assertEqual(json.loads(out.stdout)['status'],'invalid_input')

if __name__=='__main__': unittest.main()
