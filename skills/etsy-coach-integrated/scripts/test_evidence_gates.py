#!/usr/bin/env python3
"""Synthetic regression fixtures; no live market claim or network access."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from validate_evidence_gates import validate, digest
BASE = json.loads((Path(__file__).resolve().parents[1] / "assets/evidence-gate-fixture.json").read_text())

class EvidenceGates(unittest.TestCase):
    def setUp(self):
        self.p = copy.deepcopy(BASE)
    def check_bad(self, fragment):
        self.assertTrue(any(fragment in e for e in validate(self.p)), validate(self.p))
    def test_unknown_identity_and_related_test_allowed(self):
        self.assertEqual(validate(self.p), [])
    def test_short_tag_cannot_inherit_long_query(self):
        self.p['phrase_uses'][0]['relation'] = 'direct'
        self.check_bad('different query')
    def test_reordered_query_is_not_exact(self):
        self.p['actual_fields']['tags'][0] = 'grandma from gift'
        self.p['phrase_uses'][0]['phrase'] = 'grandma from gift'
        self.p['phrase_uses'][0]['relation'] = 'direct'
        self.check_bad('different query')
    def test_actual_tag_cannot_disappear_from_ledger(self):
        self.p['phrase_uses'].pop()
        self.check_bad('every actual tag')
    def test_composed_title_can_be_unmeasured(self):
        self.p['actual_fields']['title_queries'] = ['Personalized Grandson Christian Journal']
        self.p['phrase_uses'].append({'phrase':'Personalized Grandson Christian Journal','field':'title_query','relation':'composed','observation_ids':['obs2'],'numeric_claims':[],'reason':'Natural title combining truthful traits; no total volume.','product_intent_review':'Name-only lined grandson journal.'})
        self.assertEqual(validate(self.p), [])
        self.p['phrase_uses'][-1]['numeric_claims'] = [{'raw':'125'}]
        self.check_bad('cannot inherit numbers')
    def test_missing_summary_is_not_missing_raw(self):
        self.p['missing_or_requery'][0].update(query='gift for grandson from grandma',unresolved_field='competition')
        self.check_bad('already exists')
    def test_partial_raw_scan_cannot_create_requery(self):
        self.p['missing_or_requery'][0]['checked_source_ids']=['csv1']
        self.check_bad('full raw index')
    def test_unknown_cannot_be_zero(self):
        self.p['observations'][1]['metrics']['avg_searches']['raw']=0
        self.check_bad('Unknown coerced')
    def test_threshold_qualifier_must_survive(self):
        self.p['observations'][1]['metrics']['avg_searches']={'raw':'20','state':'threshold'}
        self.check_bad('qualifier lost')
    def test_baseline_overlay_cannot_replace_history(self):
        self.p['baseline']['sha256']='b'*64
        self.check_bad('different baseline')
        self.p['overlay']['baseline_sha256']='b'*64
        self.assertIn('baseline differs from external immutable lock',validate(self.p, expected_baseline_sha256='a'*64))
    def test_real_baseline_hash_detects_byte_change(self):
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'baseline.json'; file.write_text('{"status":"not_queried"}')
            lock=digest(file)
            self.p['synthetic_fixture']=False
            self.p['baseline']={'path':'baseline.json','sha256':lock}
            self.p['overlay'].update(baseline_sha256=lock,path='baseline.json',sha256=lock)
            for s in self.p['raw_sources']:
                s.update(path='baseline.json',sha256=lock)
            self.assertEqual(validate(self.p,Path(d),lock),[])
            file.write_text('{"status":"direct","avg":8033}')
            self.assertTrue(any('baseline hash mismatch'==e for e in validate(self.p,Path(d),lock)))
    def test_text_format_pass_cannot_promote_research(self):
        self.p.update(stage='text-QA-passed',gates={'text_qa':{'passed':True,'artifact_version':'fixture-v1','evidence_ref':'format-check'}})
        self.check_bad('prerequisite missing/stale: evidence')
    def test_narrow_recheck_cannot_be_final(self):
        self.p.update(release_label='final',independent_review={'independent_of_author':True,'artifact_version':'fixture-v1','verdict':'PASS','scope':['text'],'report_ref':'narrow-recheck'})
        self.check_bad('narrow/failed review')
    def test_nine_frameworks_are_not_independent_review(self):
        self.p.update(release_label='ready',independent_review={'independent_of_author':False,'artifact_version':'fixture-v1','verdict':'PASS','scope':['evidence','outcome'],'report_ref':'nine-lenses'})
        self.check_bad('independent outcome review missing')
    def test_source_month_and_matching_cannot_be_relabelled(self):
        u=self.p['phrase_uses'][0]; u.update(phrase='gift for grandson from grandma',relation='direct')
        self.p['actual_fields']['tags'][0]=u['phrase']
        self.p['missing_or_requery']=[]
        u['numeric_claims']=[{'observation_id':'obs1','metric':'avg_searches','raw':'125','state':'numeric_display','measurement_mode':'exact_only','market':'US','measurement_window':'September 2026'}]
        self.check_bad('exact-only')
        self.check_bad('market/window')
    def test_direct_qualified_numeric_join_passes(self):
        u=self.p['phrase_uses'][0]; u.update(phrase='gift for grandson from grandma',relation='direct')
        self.p['actual_fields']['tags'][0]=u['phrase']
        self.p['missing_or_requery']=[]
        o=self.p['observations'][0]
        u['numeric_claims']=[{'observation_id':'obs1','metric':'avg_searches','raw':'125','state':'numeric_display','measurement_mode':o['measurement_mode'],'market':o['market'],'market_verification':o['market_verification'],'measurement_window':o['measurement_window']}]
        self.assertEqual(validate(self.p),[])
    def test_numeric_label_cannot_hide_unknown(self):
        self.p['observations'][1]['metrics']['avg_searches']['state']='numeric_display'
        self.check_bad('not a qualified')
    def test_native_zero_ui_dash_not_observed_zero(self):
        self.p['observations'][1]['metrics']['google_searches']={'raw':'0','ui_raw':'-','state':'observed_zero'}
        self.check_bad('discrepancy is unresolved')
    def test_threshold_and_zero_preserved_as_different_states(self):
        self.p['observations'][1]['metrics']={'average':{'raw':'< 20','state':'threshold'},'Sep 2026':{'raw':'0','state':'observed_zero'}}
        self.assertEqual(validate(self.p),[])
    def test_category_guess_not_verified_coverage(self):
        self.p['category_attribute_coverage']={'state':'verified'}
        self.check_bad('actual source/values')
    def test_twenty_briefs_not_image_exports(self):
        self.p.update(stage='image-QA-passed',competitor_review_refs=['actual-page-review'])
        self.p['gates']={k:{'passed':True,'artifact_version':'fixture-v1','evidence_ref':'scoped-check'} for k in ['evidence','text_qa','image_qa']}
        self.p['gates']['image_qa'].update(accepted_count=0,required_count=20)
        self.check_bad('not accepted exports')
    def test_release_scope_cannot_jump_to_production(self):
        self.p.update(stage='evidence-qualified',release_label='production-ready',release_scope='image_production',competitor_review_refs=['actual-page-review'])
        self.p['gates']['evidence']={'passed':True,'artifact_version':'fixture-v1','evidence_ref':'source-review'}
        self.check_bad('release scope exceeds completed stage')
    def test_approved_not_applied(self):
        self.p.update(stage='applied',images_required=False,competitor_review_refs=['actual-page-review'])
        self.p['gates']={k:{'passed':True,'artifact_version':'fixture-v1','evidence_ref':'scoped-check'} for k in ['evidence','text_qa','owner_approval']}
        self.check_bad('prerequisite missing/stale: applied')

if __name__ == '__main__':
    unittest.main(verbosity=2)
