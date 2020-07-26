from typing import List, Optional
from typing_extensions import TypedDict

class GML_LayoutItemTextSegment(TypedDict):
    startOffset:Optional[str]
    endOffset:str
    content:str
class GML_NormalizedVertice(TypedDict):
    x:float
    y:float
class GML_BoundingPoly(TypedDict):
    normalizedVertices:List[GML_NormalizedVertice]
class GML_LayoutItem(TypedDict):
    textSegment:GML_LayoutItemTextSegment
    pageNumber:int
    boundingPoly:GML_BoundingPoly
    textSegmentType:str

__all__ = (GML_LayoutItemTextSegment,GML_BoundingPoly,GML_LayoutItem,GML_NormalizedVertice)