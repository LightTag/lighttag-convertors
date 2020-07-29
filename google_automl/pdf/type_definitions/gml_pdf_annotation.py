from typing import List, Optional
from typing_extensions import TypedDict

class GML_PDF_AnnotationTextSegment(TypedDict):
    startOffset: Optional[str]
    endOffset: str
class GML_PDF_AnnotationTextExtraction(TypedDict):
    textSegment:GML_PDF_AnnotationTextSegment
class GML_PDF_Annotation(TypedDict):
    displayName :str
    textExtraction:GML_PDF_AnnotationTextExtraction

