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
        # Phone number parts (US format)
        area_code = "919"
        prefix = "555"
        line_number = "1234"

        # Positive test case — valid phone number
        text = f"My number is {area_code}-{prefix}-{line_number}."
        result = analyze_text(text, ['PHONE_NUMBER'])

        # Check that one PHONE_NUMBER was detected
        self.assertEqual(len(result), 1, "Should have found 1 PHONE_NUMBER so length should be 1")

        # Verify the correct entity type
        self.assertEqual(result[0].entity_type, "PHONE_NUMBER", "PHONE_NUMBER entity type is expected")

        # Negative test case — no phone number present
        text = "Let's meet at the library later today."
        result = analyze_text(text, ['PHONE_NUMBER'])

        # Verify no PHONE_NUMBER was detected
        self.assertEqual(len(result), 0, "Negative test case should not find a result")



    def test_us_passport(self):
        """Test US_PASSPORT functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
