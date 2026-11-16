#!/usr/bin/env python3
import copy,json,pathlib,unittest,tempfile,subprocess,sys
from validate_coach_assurance import check
FIX=json.loads((pathlib.Path(__file__).parents[1]/'assets/coach-assurance-fixture.json').read_text())
class AssuranceTests(unittest.TestCase):
 def setUp(self):self.p=copy.deepcopy(FIX)
 def failcheck(self):self.assertTrue(check(self.p))
 def test_justified_unknown_identity_can_pass(self):self.assertEqual(check(self.p),[])
 def test_low_threshold_identity_can_pass(self):
  t=self.p['term_reviews'][0];t.update(volume_state='threshold',evidence='limited',risks=['limited_volume','scope_unknown']);self.assertEqual(check(self.p),[])
 def test_product_mismatch_high_volume_rejected(self):self.p['term_reviews'][1]['fit']='mismatch';self.failcheck()
 def test_high_volume_not_sufficient(self):self.p['term_reviews'][1]['volume_only_decision']=True;self.failcheck()
 def test_unknown_not_measured_demand(self):self.p['term_reviews'][0]['decision']='demand_supported_test';self.failcheck()
 def test_unknown_risk_cannot_be_hidden(self):self.p['term_reviews'][0]['risks']=[];self.failcheck()
 def test_research_join_not_transferable(self):self.p['term_reviews'][1]['exact_phrase_join']=False;self.failcheck()
 def test_scope_unverified_not_us(self):self.p['term_reviews'][0]['claims_current_US_demand']=True;self.failcheck()
 def test_average_or_single_month_not_trend(self):self.p['term_reviews'][1].update(claims_trend=True,trend_basis='single_month');self.failcheck()
 def test_actual_tags_not_traffic(self):self.p['term_reviews'][1]['tags_prove_traffic']=True;self.failcheck()
 def test_risk_disposition_required(self):self.p['term_reviews'][0]['risk_disposition']='';self.failcheck()
 def test_change_evidence_required(self):self.p['term_reviews'][0]['change_evidence']='';self.failcheck()
 def test_each_actual_tag_reviewed(self):self.p['artifact']['selected_tags'].append('cross journal');self.failcheck()
 def test_duplicate_names_not_nine_judges(self):self.p['reviews'][1]['independent']=False;self.failcheck()
 def test_author_cannot_judge_independently(self):self.p['reviews'][1]['author_participation']=True;self.failcheck()
 def test_consensus_preload_not_independent(self):self.p['reviews'][1]['preloaded_consensus']=True;self.failcheck()
 def test_missing_specialty_blocks_release(self):self.p['reviews'][0]['roles']=['B','C','D'];self.failcheck()
 def test_single_framework_blocks_release(self):
  for r in self.p['reviews']:r['source_families']=['one_framework']
  self.failcheck()
 def test_open_finding_blocks_release(self):self.p['reviews'][1]['outcome']='REVISE';self.failcheck()
 def test_original_gate_required(self):self.p['base_evidence_gate']='BLOCKED';self.failcheck()
 def test_live_coach_claim_rejected(self):self.p['claims_live_coach_participation']=True;self.failcheck()
 def test_new_queries_need_vault_reuse(self):self.p['new_queries']=[{'phrase':'grandson keepsake'}];self.failcheck()
 def test_draft_can_retain_independence_gap(self):self.p.update(scope='draft',reviews=[],base_evidence_gate='BLOCKED');self.assertEqual(check(self.p),[])
 def test_unknown_date_not_automatically_stale(self):self.p['term_reviews'][0]['source_date']=None;self.assertEqual(check(self.p),[])
class IndependentBoundaryTests(unittest.TestCase):
 def setUp(self):self.p=copy.deepcopy(FIX)
 def failcheck(self):self.assertTrue(check(self.p))
 def test_same_run_cannot_author_and_judge(self):self.p['reviews'][1]['run_id']=self.p['reviews'][0]['run_id'];self.failcheck()
 def test_empty_independent_scope_rejected(self):self.p['reviews'][1]['roles']=[];self.failcheck()
 def test_hidden_blocked_role_rejected(self):self.p['reviews'][1]['role_outcomes']['A']='BLOCKED';self.failcheck()
 def test_role_verdict_required(self):self.p['reviews'][1].pop('role_outcomes');self.failcheck()
 def test_base_gate_hash_bound(self):self.p['base_evidence_gate']['artifact_sha256']='f'*64;self.failcheck()
 def test_base_gate_version_bound(self):self.p['base_evidence_gate']['artifact_version']='old';self.failcheck()
 def test_bare_base_pass_not_accepted(self):self.p['base_evidence_gate']='PASS';self.failcheck()
 def test_monthly_series_must_not_be_false_gap(self):
  self.p['new_queries']=[{'phrase':'christian journal','vault_version_checked':'v4','existing_source_ids_checked':['monthlyEvidence'],'unresolved_field':'15-month sequence','unresolved_field_key':'monthly_series','why_existing_insufficient':'claim missing','decision_changed':'trend','stop_condition':'read series','source_sections_checked':['terms','observations','monthlyEvidence','raw_source_index'],'request_kind':'missing'}];self.failcheck()
class InvalidPacketTests(unittest.TestCase):
 def test_null_reviews_fail_cleanly(self):
  p=copy.deepcopy(FIX);p['reviews']=None
  with tempfile.TemporaryDirectory() as d:
   f=pathlib.Path(d)/'packet.json';f.write_text(json.dumps(p));run=subprocess.run([sys.executable,str(pathlib.Path(__file__).with_name('validate_coach_assurance.py')),str(f)],capture_output=True,text=True);result=json.loads(run.stdout);self.assertNotEqual(run.returncode,0);self.assertEqual(result['status'],'REVISE');self.assertIn('invalid packet',result['errors'][0]);self.assertNotIn('Traceback',run.stderr)
if __name__=='__main__':unittest.main(verbosity=2)
