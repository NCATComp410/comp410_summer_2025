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
