import unittest
import os

from google_automl.pdf.gml_pdf_to_lighttag import gml_json_to_lighttag_example

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'outml_annotation_data.jsonl')

class TestGMLToLightTag(unittest.TestCase):
    def test_it_works(self):
        '''
        Laconically named test, but if it works we got all of the field names correct
        :return:
        '''
        gml_json_to_lighttag_example(TESTDATA_FILENAME)
