"""Some unit tests for the PII scan module."""
import unittest
import os
import ast
from pii_scan import show_aggie_pride, analyze_text


class TestPIIScan(unittest.TestCase):
    """Test cases for PII scan module."""
    def test_aggie_pride(self):
        """Test to make sure the Aggie Pride function works"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_base_supported_entities(self):
        """Test to make sure the default expected supported entities are returned"""
        EMPTY_TEXT = ''
        EMPTY_ENTITY_LIST = []
        results = analyze_text(text=EMPTY_TEXT, entity_list=EMPTY_ENTITY_LIST, show_supported=True)
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
        from pathlib import Path
        for file in Path(os.path.dirname(__file__)).glob('test_*.py'):
            with file.open(encoding='utf-8') as f:
                tree = ast.parse(f.read(), filename=file)
                for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            method_name = node.name
                            # Skip legitimate non-test methods like setUp, tearDown, and private methods
                            if method_name in {'setUp', 'tearDown'} or method_name.startswith('_'):
                                continue
                            self.assertTrue(method_name.startswith('test'),
                                            f'Method name does not start with test: def {method_name} in {file}')
