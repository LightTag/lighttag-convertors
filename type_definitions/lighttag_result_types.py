import typing
from typing import  List, Optional,Dict,Any
from typing_extensions import TypedDict
class Testament(TypedDict):
    annotator_id:int
    annotator:str
    timestamp:str

class Annotation(TypedDict):
    example_id: str
    start: int
    end: int
    tag: str
    tag_id: str
    tagged_token_id: str
    value: str
    reviewed: bool
    correct: Optional[bool]
    annotated_by: List[Testament]


class Classification(TypedDict):
    example_id:str
    classname:str
    class_id:str
    classified_by:List[Testament]



class Example(TypedDict):
    example_id:str
    content:str
    metadata:Dict[Any,Any]
    seen_by:List[Testament]
    annotations:List[Annotation]
    classifications:List[Classification]
