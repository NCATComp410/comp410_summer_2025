"""Some unit tests for the PII scan module."""
import unittest
import re
import os
from pii_scan import show_aggie_pride, analyze_text


class TestPIIScan(unittest.TestCase):
    """Test cases for PII scan module."""
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_base_supported_entities(self):
        """Test to make sure the default expected supported entities are returned"""
        results = analyze_text('', [], show_supported=True)
        supported_entities = ['IP_ADDRESS',
                              'MEDICAL_LICENSE',
                              'LOCATION',
                              'EMAIL_ADDRESS',
                              'DATE_TIME',
                              'ORGANIZATION',
                              'CREDIT_CARD',
                              'CRYPTO',
                              'AU_MEDICARE',
                              'AU_ABN',
                              'PHONE_NUMBER',
                              'US_PASSPORT',
                              'IBAN_CODE',
                              'AU_TFN',
                              'US_BANK_NUMBER',
                              'NRP',
                              'UK_NHS',
                              'UK_NINO',
                              'US_SSN',
                              'PERSON',
                              'URL',
                              'US_ITIN',
                              'US_DRIVER_LICENSE',
                              'AU_ACN',
                              'ORGANIZATION',
                              'IT_VAT_CODE',
                              'IT_IDENTITY_CARD',
                              'IT_DRIVER_LICENSE',
                              'IT_PASSPORT',
                              'IT_FISCAL_CODE',
                              'FI_PERSONAL_IDENTITY_CODE',
                              'PL_PESEL',
                              'ES_NIE',
                              'ES_NIF',
                              'ABA_ROUTING_NUMBER',
                              'IN_VEHICLE_REGISTRATION',
                              'IN_PASSPORT',
                              'IN_VOTER',
                              'IN_AADHAAR',
                              'IN_PAN']
        
        for entity in supported_entities:
            self.assertIn(entity, results)

    def test_starts_with_test(self):
        """Test to make sure all test methods start with test"""
        # In order to run as a test case the method name must start with test
        # This test checks to make sure all defines within test files start with test
        # This is a common mistake that can cause tests to be skipped
        for file in os.listdir('.'):
            if file.endswith('.py') and file.startswith('test_'):
                with open(file, encoding='utf-8') as f:
                    for line in f:
                        # make sure everything that looks like a method name starts with test
                        m = re.search(r'\s*def (\w+)', line)
                        if m:
                            self.assertTrue(m.group(1).startswith('test'),
                                            'Method name does not start with test: def ' + m.group(1) + ' in ' + file)
