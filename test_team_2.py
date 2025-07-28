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
        start = "4111"
        mid = "1111"
        end = "1111 1111"
        # Positive test case
        result = analyze_text(f"My credit card number is {start} {mid} {end}", ['CREDIT_CARD'])
        # Check to make sure there is one result
        self.assertEqual(len(result), 1, "Should have found 1 CREDIT_CARD so length should be 1")
        # Check that a CREDIT_CARD was actually found
        self.assertEqual(result[0].entity_type, "CREDIT_CARD", "CREDIT_CARD entity type is expected")

        # Negative test case
        result = analyze_text("My credit card number is 1234-5678-9101 1213", ['CREDIT_CARD'])
        # Check to make sure there is no result
        self.assertEqual(len(result), 0, "Negative test case should not find a result")

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
        #Ari Rozier: Team 2
        """Test EMAIL_ADDRESS functionality"""
        # positive test case
        result = analyze_text('example@example.com', ['EMAIL_ADDRESS'])

        #error handeling if more than 1 submission
        self.assertEqual(len(result), 1, 'Only 1 submission is expected')
        #error handeling if result is NOT an Email Address Type
        self.assertEqual(result[0].entity_type, 'EMAIL_ADDRESS', 'Should have found a valid email address. Including the name and domain type.')

        #negative test case
        result = analyze_text('example123.com', ['EMAIL_ADDRESS'])
        #error handeling if more than 1 submission
        self.assertEqual(len(result), 0, 'There shouldnt be anything in the user test case')


if __name__ == '__main__':
    unittest.main()
