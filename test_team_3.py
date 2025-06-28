"""Unit test file for team 3"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_3(unittest.TestCase):
    """Test team 3 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""


if __name__ == '__main__':
    unittest.main()
