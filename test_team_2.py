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
