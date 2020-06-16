from typing import Optional, List

from typing_extensions import TypedDict
class LTSuggestionInput(TypedDict):
    example_id:str
    start:int
    end:int
    tag:str
    text:Optional[str]

class LTExampleSuggestionsWithTestament(TypedDict):
    '''
    Sometimes models will have seen an example without making any predictions.
    In that case, we still want to record that the model had seen the example. In LightTag we call that a Testament.
    '''
    suggestions:List[LTSuggestionInput]
    seen_example_id:str

class LTSuggestionsWithTestaments(TypedDict):
    '''
    Container for results of converting the output of a model over many examples into a format LightTag will consume
    '''
    seen_example_ids:List[str] # The list of all examples the model has seen
    suggestions:List[LTSuggestionInput] #The models suggestions if any
