from typing import List
from typing_extensions import TypedDict
from .lighttag_metadata_types import Schema
from .lighttag_result_types import LTExample


class JobResult(TypedDict):
    name:str
    id:str
    examples:List[LTExample]
    schema:Schema
__all__ = (JobResult,)