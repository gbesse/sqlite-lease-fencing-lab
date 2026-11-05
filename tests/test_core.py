import unittest
from sqlite_lease_fencing_lab.core import run
class DomainTests(unittest.TestCase):
 def test_stale_rejected(self):
  x=run({});self.assertEqual(x['fenced']['final_value'],'B-current');self.assertFalse(x['fenced']['trace'][-1]['accepted'])
 def test_unguarded_counterexample(self):self.assertEqual(run({})['unfenced']['final_value'],'A-stale')
 def test_monotone(self):self.assertEqual([r['token']for r in run({})['fenced']['trace']],[1,2,1])
