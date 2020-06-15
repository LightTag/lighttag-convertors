from typing import Optional

from typing_extensions import TypedDict
class LTSuggestionInput(TypedDict):
    example_id:str
    start:int
    end:int
    tag:str
    text:Optional[str]