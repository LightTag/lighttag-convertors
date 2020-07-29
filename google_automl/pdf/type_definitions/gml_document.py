from typing import List
from typing_extensions import TypedDict

from google_automl.pdf.type_definitions.gml_layout import GML_PDF_LayoutItem


class GML_PDF_DocumentText(TypedDict):
    content:str
class GML_PDF_DocumentDimensions(TypedDict):
    unit:str
    width:int
    height:int

class GML_PDF_Document(TypedDict):
    documentText:GML_PDF_DocumentText
    layout:List[GML_PDF_LayoutItem]
    documentDimensions:GML_PDF_DocumentDimensions
    pageCount:int