"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
        pre = '123'
        mid = '12'
        suffix = '1234'
        # Positive test case
        result = analyze_text(f'My SSN is {pre}-{mid}-{suffix}', ['US_SSN'])
        # Check to make sure there is one result
        self.assertEqual(len(result), 1, 'Should have found 1 SSN so length should be 1')
        # Check that a SSN was actually found
        self.assertEqual(result[0].entity_type, 'US_SSN', 'US_SSN entity type is expected')

        # Negative test case
        result = analyze_text('My SSN is 123-45-6789', ['US_SSN'])
        # Check to make sure there is no result
        self.assertEqual(len(result), 0, 'Negative test case should not find a result')


if __name__ == '__main__':
    unittest.main()
