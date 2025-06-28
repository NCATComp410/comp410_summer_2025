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
        """Test PERSON functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
