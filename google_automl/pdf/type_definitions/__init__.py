from typing import List
from typing_extensions import TypedDict

from google_automl.pdf.type_definitions.gml_document import GML_PDF_Document
from google_automl.pdf.type_definitions.gml_pdf_annotation import GML_PDF_Annotation


class GML_PDF_JSONLExample(TypedDict):
    '''
    Represents an entire JSONL provided by Google AutoML (pdf)
    One GML_JSONLExample corresponds to one LightTag Example
    '''
    document:GML_PDF_Document # Data about the document
    annotations:List[GML_PDF_Annotation] #User made annotations




class LTInputExampleFromGML(TypedDict):
    '''
    The format of an example LightTag wants from Automl
    '''
    content:str
    gml: GML_PDF_JSONLExample
    jsonl_filename: str  # The jsonl filename used