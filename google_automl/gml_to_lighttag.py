import json
import os
from typing import List

from google_automl.type_definitions import (
    GML_JSONLExample,
    LTInputExampleFromGML,
)


def gml_example_to_lighttag_example(
    gml: GML_JSONLExample, filename: str
) -> LTInputExampleFromGML:
    '''

    :param gml: The parsed contents of the google JSONL
    :param filename:  The name of the jsonl (not full path)
    :return:  A LightTag example with the GML data and filename in it's metadata
    '''
    content = gml["document"]["documentText"].pop("content")
    lt_example: LTInputExampleFromGML = LTInputExampleFromGML(
        content=content, gml=gml,jsonl_filename=filename
    )
    return lt_example

def gml_json_to_lighttag_example(
        filepath:str
) -> LTInputExampleFromGML:
    '''
    Gets the path to a GML jsonl and returns the LTInputExampleFromGML object
    :param filepath:
    :return:
    '''
    with open(filepath) as f:
        filename = f.name
        gml :GML_JSONLExample = json.load(f)
        return gml_example_to_lighttag_example(gml,filename=filename)
def gml_dir_to_lighttag_examples(path:str) ->List[LTInputExampleFromGML]:
    '''
    Iterates over all JSONls in the provided path and returns a list of  LTInputExampleFromGML
    :param path: The path to iterate over
    :return: A list of LTInputExampleFromGML
    '''
    results : List[LTInputExampleFromGML] =[]
    for fname in os.listdir(path):
        if fname.endswith('jsonl'):
            filepath = os.path.join(path,fname)
            results.append(gml_json_to_lighttag_example(filepath))
    return results
