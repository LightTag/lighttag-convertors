from typing import List
from typing_extensions import TypedDict
from type_definitions.lighttag_metadata_types import Schema
from type_definitions.lighttag_result_types import Example


class JobResult(TypedDict):
    name:str
    id:str
    examples:List[Example]
    schema:Schema
