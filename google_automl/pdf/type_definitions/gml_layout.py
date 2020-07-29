from typing import List, Optional
from typing_extensions import TypedDict

class GML_PDF_LayoutItemTextSegment(TypedDict):
    startOffset:Optional[str]
    endOffset:str
    content:str
class GML_PDF_NormalizedVertice(TypedDict):
    x:float
    y:float
class GML_PDF_BoundingPoly(TypedDict):
    normalizedVertices:List[GML_PDF_NormalizedVertice]
class GML_PDF_LayoutItem(TypedDict):
    textSegment:GML_PDF_LayoutItemTextSegment
    pageNumber:int
    boundingPoly:GML_PDF_BoundingPoly
    textSegmentType:str

__all__ = (GML_PDF_LayoutItemTextSegment, GML_PDF_BoundingPoly, GML_PDF_LayoutItem, GML_PDF_NormalizedVertice)