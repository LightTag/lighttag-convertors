from typing import List, Optional
from typing_extensions import TypedDict

class GML_AnnotationTextSegment(TypedDict):
    startOffset: Optional[str]
    endOffset: str
class GML_AnnotationTextExtraction(TypedDict):
    textSegment:GML_AnnotationTextSegment
class GML_Annotation(TypedDict):
    displayName :str
    textExtraction:GML_AnnotationTextExtraction

