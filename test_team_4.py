"""Unit test file for team 4"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_4(unittest.TestCase):
    """Test team 4 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""

    
    def test_person(self):
        """Test PERSON detection for full names with variations"""
    
    # Positive Test Case 1: Standard full name with middle initial
        test_str = "Emily R. Davis"
        result = analyze_text(test_str, ['PERSON'])

        self.assertGreater(len(result), 0, 'No person detected in standard name format')
        self.assertEqual(result[0].entity_type, 'PERSON')
        self.assertGreaterEqual(result[0].score, 0.85)

    # Positive Test Case 2: Name with hyphen and apostrophe
        test_str = "Anne-Marie O'Connor"
        result = analyze_text(test_str, ['PERSON'])

        self.assertGreater(len(result), 0, 'No person detected with hyphen or apostrophe')
        self.assertEqual(result[0].entity_type, 'PERSON')
        self.assertGreaterEqual(result[0].score, 0.85)

    # Positive Test Case 3: Name with suffix
        test_str = "Michael Thompson Jr."
        result = analyze_text(test_str, ['PERSON'])

        self.assertGreater(len(result), 0, 'No person detected with suffix')
        self.assertEqual(result[0].entity_type, 'PERSON')
        self.assertGreaterEqual(result[0].score, 0.85)

    # Negative Test Case: Random non-name input
        test_str = "NotARealName123"
        result = analyze_text(test_str, ['PERSON'])

        self.assertEqual(len(result), 0, 'Expected no person entity detection')


    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
