from typing import List, Optional
from typing_extensions import TypedDict

from google_automl.type_definitions.gml_layout import GML_LayoutItem


class GML_DocumentText(TypedDict):
    content:str
class GML_DocumentDimensions(TypedDict):
    unit:str
    width:int
    height:int

class GML_Document(TypedDict):
    documentText:GML_DocumentText
    layout:List[GML_LayoutItem]
    documentDimensions:GML_DocumentDimensions
    pageCount:int