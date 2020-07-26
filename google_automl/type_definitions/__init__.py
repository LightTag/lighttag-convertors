from typing import List, Optional
from typing_extensions import TypedDict

from google_automl.type_definitions.gml_annotation import GML_Annotation
from google_automl.type_definitions.gml_document import GML_Document


class GML_JSONLExample(TypedDict):
    '''
    Represents an entire JSONL provided by Google AutoML (pdf)
    One GML_JSONLExample corresponds to one LightTag Example
    '''
    document:GML_Document # Data about the document
    annotations:List[GML_Annotation] #User made annotations




class LTInputExampleFromGML(TypedDict):
    '''
    The format of an example LightTag wants from Automl
    '''
    content:str
    gml: GML_JSONLExample
    jsonl_filename: str  # The jsonl filename used