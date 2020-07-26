from typing import  List, Optional, Dict, Any
from typing_extensions import TypedDict

class Tag(TypedDict):
    name: str
    description: str
    id: str
    schema_id: str


class ClassificationType(TypedDict):
    name: str
    description: str
    id: str
    schema_id: str


class SuggestionModel:
    url: str
    name: str
    metadata: Dict[Any, Any]
    schema_id: str


class Schema(TypedDict):
    id: str
    name: str
    archived: bool
    tags: List[Tag]
    classification_types: List[ClassificationType]
    models: List[SuggestionModel]


class Dataset(TypedDict):
    id: str
    slug: str
    url: str
    name: str
    id_field: str
    content_field: str
    aggregation_field: str
    order_field: str
    project_id: str
    upload_status: str
    archived: bool
    editable: bool
__all__ = (Dataset,Schema,SuggestionModel,ClassificationType,Tag)