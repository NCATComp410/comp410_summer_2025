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
        #Positive test case
        test_str = "My bank account number is 12345678901."
        result = analyze_text(test_str, ['US_BANK_NUMBER'])
        self.assertEqual(len(result), 1, 'No bank number detected ')
        self.assertEqual(result[0].entity_type, 'US_BANK_NUMBER')
        #Negative test case
        test_str = "Number 201213"
        result = analyze_text(test_str,['US_BANK_NUMBER'] )
        self.assertEqual(len(result), 0, 'Should have found 0 Bank Numbers')

    def test_us_driver_license(self):

        # Positive Test case
        result = analyze_text('My Drivers License number is 0000123122424' , ['US_DRIVER_LICENSE'])
        print (result)
        # Make sure 1 valid result was found
        self.assertEqual(len(result), 1)
        # Make sure it was a US_DRIVER_LICENSE
        self.assertEqual(result[0].entity_type, 'US_DRIVER_LICENSE', 'Valid License Number')

        # Negative test case
        result = analyze_text('My Drivers License number is XYZ999' , ['US_DRIVER_LICENSE'])
        self.assertEqual(len(result), 0, 'Invalid License Number')

    def test_us_itin(self):
    """Test US_ITIN functionality"""

    # Positive Test case
    result = analyze_text('My ITIN is 912-70-1234', ['US_ITIN'])
    print(result)
    # Make sure 1 valid result was found
    self.assertEqual(len(result), 1)
    # Make sure it was a US_ITIN
    self.assertEqual(result[0].entity_type, 'US_ITIN', 'Valid ITIN')

    # Negative Test case
    result = analyze_text('My ITIN is 123-45-6789', ['US_ITIN'])  # This is a typical SSN format
    self.assertEqual(len(result), 0, 'Invalid ITIN')


if __name__ == '__main__':
    unittest.main()
