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
        # Positive test case
        crypto_key = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'  # Valid BTC address Presidio should detect
        result = analyze_text(f"My BTC address is {crypto_key}", ['CRYPTO'])
        # Check if crypto was detected
        self.assertEqual(len(result), 1, 'Should have found 1 CRYPTO so length should be 1')
        self.assertEqual(result[0].entity_type, 'CRYPTO', 'CRYPTO entity type is expected')
        # Negative test case
        result = analyze_text("This is a normal sentence with no keys or sensitive data.", ['CRYPTO'])
        self.assertEqual(len(result), 0, 'Should NOT have found any CRYPTO so length should be 0')





    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
