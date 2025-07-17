"""PII Scan"""
import re
import logging
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, RecognizerResult
from presidio_analyzer.predefined_recognizers import (
    ItDriverLicenseRecognizer,
    ItVatCodeRecognizer,
    ItFiscalCodeRecognizer,
    ItIdentityCardRecognizer,
    ItPassportRecognizer,
    EsNieRecognizer,
    EsNifRecognizer,
    PlPeselRecognizer,
    FiPersonalIdentityCodeRecognizer,
    AbaRoutingRecognizer,
    AuAbnRecognizer,
    AuAcnRecognizer,
    AuTfnRecognizer,
    AuMedicareRecognizer
)
from presidio_anonymizer import AnonymizerEngine
import requests

# make sure en_core_web_lg is loaded correctly
# this can also be achieved with
# python -m spacy download en_core_web_lg
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Configure logging to DEBUG level when needed
# logging.basicConfig(level=logging.DEBUG)
# Configure logging to INFO level when needed
# logging.basicConfig(level=logging.INFO)
# By default only critical logs will be printed
logging.basicConfig(level=logging.CRITICAL)

# Create an analyzer object
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
# Add some language specific recognizers as english instead of default language
registry.add_recognizer(ItDriverLicenseRecognizer(supported_language='en'))
registry.add_recognizer(ItVatCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItFiscalCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItIdentityCardRecognizer(supported_language='en'))
registry.add_recognizer(ItPassportRecognizer(supported_language='en'))
registry.add_recognizer(EsNieRecognizer(supported_language='en'))
registry.add_recognizer(EsNifRecognizer(supported_language='en'))
registry.add_recognizer(PlPeselRecognizer(supported_language='en'))
registry.add_recognizer(
    FiPersonalIdentityCodeRecognizer(supported_language='en'))
registry.add_recognizer(AbaRoutingRecognizer(supported_language='en'))
registry.add_recognizer(AuAbnRecognizer(supported_language='en'))
registry.add_recognizer(AuAcnRecognizer(supported_language='en'))
registry.add_recognizer(AuTfnRecognizer(supported_language='en'))
registry.add_recognizer(AuMedicareRecognizer(supported_language='en'))


# Create an analyzer object
# log_decision_process=True will log the decision process for debugging
analyzer = AnalyzerEngine(registry=registry, log_decision_process=False)
anonymizer = AnonymizerEngine()


def show_aggie_pride():
    """Show Aggie Pride"""
    return "Aggie Pride - Worldwide"


def anonymize_text(text: str, entity_list: list) -> str:
    """
    Anonymize the text using the entity list
    :param text: the text to be anonymized
    :param entity_list: the list of entities to be anonymized
           https://microsoft.github.io/presidio/supported_entities/
    """
    # Call analyzer to get results
    results = analyze_text(text=text, entity_list=entity_list)

    # Analyzer results are passed to the AnonymizerEngine for anonymization
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    return anonymized_text.text


def anonymize_data(data: list) -> None:
    """
    Anonymize the text using the entity list
    :param data: the data to be anonymized
    """
    for i, item in enumerate(data):
        if item:
            if item.startswith('#'):
                print(item)
            else:
                print(f'ID:{i}:Original  : {item}')
                print(f'ID:{i}:Anonymized: {anonymize_text(item, [])}')


def analyze_text(text: str, entity_list: list, show_supported=False) -> list[str] | list[RecognizerResult]:
    """
    Analyze the text using the entity list
    :param text: the text to be analyzed
    :param entity_list: the list of entities to be analyzed
           https://microsoft.github.io/presidio/supported_entities/
    :param show_supported: show the supported entities
    """
    # Show all entities that can be detected for debugging
    if show_supported:
        return analyzer.get_supported_entities()
    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                               entities=entity_list,
                               language='en',
                               return_decision_process=True)  # return decision process details

    return results


def read_data() -> list:
    """
    Reads data from a secure file using a secret key stored in .env
    :return: list of lines from the file
    """
    # Load SECRET from .env file
    with open('.env', encoding='utf-8') as f:
        for line in f.readlines():
            m = re.search(r'SECRET="(\w+)"', line)
            if m:
                secret = m.group(1)
                break
            else:
                raise RuntimeError("SECRET not found in .env file")

    # Construct the URL from the API key
    header = 'https://drive.google.com/uc?export=download&id=1Madj8otKjwwOO353nL_'
    url = requests.get(header + secret, timeout=10)

    # Return the data as a list of lines
    return url.text.split('\n')


if __name__ == '__main__':
    print(show_aggie_pride())
