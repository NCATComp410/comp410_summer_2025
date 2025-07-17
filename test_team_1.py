"""Unit test file for team 1"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 

class TestTeam_1(unittest.TestCase):
    """Test team 1 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_au_abn(self):
        """Test AU_ABN functionality"""
        # Positive test: should detect AU_ABN
        text_with_abn = "Our ABN is 51 824 753 556 and it's valid."
        results = analyze_text(text_with_abn, ["AU_ABN"])
        self.assertGreater(len(results), 0, "Should detect AU_ABN")
        self.assertEqual(results[0].entity_type, "AU_ABN", "Detected entity should be AU_ABN")

        # Negative test: no AU_ABN present
        text_without_abn = "This text contains no business identifier."
        results = analyze_text(text_without_abn, ["AU_ABN"])
        self.assertEqual(len(results), 0, "Should not detect AU_ABN in plain text")

    def test_au_acn(self):
        """Test AU_ACN functionality"""

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""
        pre = 2456
        mid = 78129
        suffix = 9
        #Positive test: should detect AU_MEDICARE
        results = analyze_text(f'Our AU_MEDICARE is {pre} {mid} {suffix}', ['AU_MEDICARE'])
        #Check to make sure there is one result
        self.assertEqual(len(results), 1, "Should detect AU_MEDICARE")
        #Check to make sure AU_MEDICARE was found
        self.assertEqual(results[0].entity_type, "AU_MEDICARE", "Detected entity should be AU_MEDICARE")

        #Negative Test: Shouldn't Detect AU_MEDICARE
        text_without_aumedicare = "This contains no buisness identifier"
        results = analyze_text(text_without_aumedicare, ["AU_MEDICARE"])
        self.assertEqual(len(results), 0, "Should not detect AU_MEDICARE in plain text")

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
