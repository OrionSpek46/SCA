# tests/test_analyzer.py

import unittest
from analyzer.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def test_hard_coded_password(self):
        analyzer = Analyzer('tests/sample_code/hard_coded_password.py')
        analyzer.run()
        issues = analyzer.get_issues()
        self.assertTrue(any(issue['rule_id'] == 'SCP001' for issue in issues))

if __name__ == '__main__':
    unittest.main()
