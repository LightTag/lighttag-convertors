from typing import  List, Dict, Any
from typing_extensions  import TypedDict

class Mention(TypedDict):
    startOffset:int
    endOffset:int
    normalized:str
class Entity(TypedDict):
    mentions:List[Mention]
    type:str

class EntitiesList(TypedDict):
    type:str #always list
    itemType:str  #always entities
    items:List[Entity]
class ADMAttributes(TypedDict):
    entities:EntitiesList
class ADMDoc(TypedDict):
    version:str
    data:str # The original text
    attributes:ADMAttributes
    documentMetadata:Dict[Any,Any]