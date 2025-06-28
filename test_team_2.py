"""Unit test file for team 2"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_2(unittest.TestCase):
    """Test team 2 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
