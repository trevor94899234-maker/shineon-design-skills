#!/usr/bin/env python3
"""Verify the dated ranking keeps source metadata and roster membership intact."""
import json,pathlib,unittest
R=pathlib.Path(__file__).parents[1]/'references'
ROSTER=json.loads((R/'active-coach-roster.json').read_text())
RANK=json.loads((R/'coach-ranking-2026-10-09.json').read_text())
def records(x,sid):
 if isinstance(x,dict):
  if (x.get('source_id') or x.get('id'))==sid and x.get('url'):yield x
  for v in x.values():yield from records(v,sid)
 elif isinstance(x,list):
  for v in x:yield from records(v,sid)
def pub(s):
 return s.get('published_at') or s.get('date_published') or s.get('publication_date') or s.get('published_date') or s.get('published') or s.get('published_at_utc') or s.get('published_utc') or s.get('displayed_publication_date') or s.get('watch_metadata',{}).get('date_published') or s.get('latest_observed',{}).get('published')
class RankingIntegrity(unittest.TestCase):
 def test_all_admitted_people_exactly_once(self):
  names=[r['name'] for r in RANK['rankings']];self.assertEqual(len(names),len(set(names)));self.assertEqual(set(names),{r['name'] for r in ROSTER['people']})
 def test_ranks_complete(self):self.assertEqual(sorted(r['contextual_rank'] for r in RANK['rankings']),list(range(1,31)))
 def test_dimensions_separate_no_composite(self):
  for r in RANK['rankings']:
   self.assertEqual(set(r['scores']),{'fit','impact','evidence_quality','selected_method_completeness'});self.assertNotIn('composite',r);self.assertIn('freshness',r)
 def test_source_ids_urls_and_dates_join(self):
  for r in RANK['rankings']:
   for ref in r['source_references']:
    candidates=list(records(json.loads((R/ref['ledger']).read_text()),ref['source_id']));self.assertTrue(candidates,ref['source_id']);self.assertTrue(any(c['url']==ref['url'] for c in candidates));dates=[pub(c) for c in candidates if pub(c)];self.assertTrue(not dates or ref['published'] in dates,ref['source_id'])
 def test_nested_date_regressions(self):
  dates={r['name']:r['freshness']['selected_source_latest_publication'] for r in RANK['rankings']};self.assertEqual(dates['Jesse Teaches'],'2026-09-21');self.assertEqual(dates['RJ Martinez'],'2026-10-07');self.assertEqual(dates['Courtney Nichole'],'2026-10-07')
 def test_latest_metadata_not_ignored(self):
  rows={r['name']:r for r in RANK['rankings']}
  for name in ['Starla Moore','Dylan Jahraus','Joe Robert','Mei Pak','Amy Eaton']:
   self.assertIn('subsequent_metadata_check',rows[name]['freshness']);self.assertIn('subsequent_content_status',rows[name]['freshness']['latest_observed'])
 def test_no_claim_of_full_channel_refresh(self):self.assertFalse(RANK['new_full_coach_channel_refresh_performed']);self.assertFalse(RANK['all_complete_frameworks_available'])
if __name__=='__main__':unittest.main(verbosity=2)
