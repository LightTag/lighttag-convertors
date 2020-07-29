from typing import List
from typing_extensions import TypedDict
class GML_PT_TextSegment(TypedDict):
    start_offset:str
    end_offset:str
class GML_PT_TextExtraction(TypedDict):
    text_segment:GML_PT_TextSegment
class GML_PT_TextSnippet(TypedDict):
    content:str
class GML_PT_Annotation(TypedDict):
    text_extraction:GML_PT_TextExtraction
    display_name:str
class GML_PT_JSONL(TypedDict):
    annotations:List[GML_PT_Annotation]
    text_snippet:GML_PT_TextSnippet