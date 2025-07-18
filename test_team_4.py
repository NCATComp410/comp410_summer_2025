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
        self.assertEqual(result[0].entity_type, "PHONE_NUMBER","PHONE_NUMBER entity type is expected")

        # Negative test case — no phone number present
        text = "Let's meet at the library later today."
        result = analyze_text(text, ['PHONE_NUMBER'])

        # Verify no PHONE_NUMBER was detected
        self.assertEqual(len(result), 0, "Negative test case should not find a result")

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""
        # Positive test case – valid US passport number (9 digits)
        text = "My US passport number is 123456789."
        result = analyze_text(text, ['US_PASSPORT'])

        # Check that one US_PASSPORT was detected
        self.assertGreaterEqual(len(result), 1, "Should have found at least 1 US_PASSPORT")

        # Verify the correct entity type is present
        found_passport = any(r.entity_type == "US_PASSPORT" for r in result)
        self.assertTrue(found_passport, "Expected US_PASSPORT entity to be detected")

        # Negative test case – similar format but should not be detected
        text = "My student ID number is 921."
        result = analyze_text(text, ['US_PASSPORT'])

        # Ensure no US_PASSPORT entity is detected
        found_passport = any(r.entity_type == "US_PASSPORT" for r in result)
        self.assertFalse(found_passport, "Negative test should not detect a US_PASSPORT")

    
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
        pre = 'MD'
        digits = '4488929'
        # positive test case
        result = analyze_text(f'My medical DEA certificate number is {pre}{digits}', ['MEDICAL_LICENSE'])
        # check to make sure there is one result
        self.assertEqual(len(result), 1)
        # check that a medical license was actually found
        self.assertEqual(result[0].entity_type, 'MEDICAL_LICENSE')

        # negative test case
        result = analyze_text("My medical DEA certificate number is MD1488929", ['MEDICAL_LICENSE'])
        # check to see there is no result
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
