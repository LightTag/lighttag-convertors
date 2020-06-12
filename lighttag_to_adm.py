from typing import List

from conflict_resolver import resolve_annotation_conflicts
from type_definitions.adm_types import ADMDoc, Entity, EntitiesList, ADMAttributes
from type_definitions.lighttag_job import JobResult
from type_definitions.lighttag_result_types import Example, Annotation
from utils import sort_example_annotations, make_slug
import json
import os

def convert_lighttatg_annotation_to_adm(anno: Annotation) -> Entity:
    result: Entity = {
        "type": anno["tag"].upper(),
        "mentions": [
            {
                "startOffset": anno["start"],
                "endOffset": anno["end"],
                "normalized": anno["value"],
            }
        ],
    }
    return result



def get_converted_metadata(example: Example):
    res = dict()
    for key, value in example["metadata"].items():
        if type(value) is list:
            res[key] = value
        else:
            res[key] = [ value]

    res['lighttag_example_id']= [ example['example_id'] ]
    return res


def convert_lighttag_example_to_adm(
    example: Example, reviewed_only, exclude_attributes
) -> ADMDoc:
    example = sort_example_annotations(example, reviewed_only=reviewed_only)
    example['annotations'] = resolve_annotation_conflicts(example['annotations'])
    adm_annotations: List[Entity] = [
        convert_lighttatg_annotation_to_adm(anno) for anno in example["annotations"]
    ]
    entity_list: EntitiesList = {
        "type": "list",
        "itemType": "entities",
        "items": adm_annotations,
    }
    if not exclude_attributes:
        attributes: ADMAttributes = {"entities": entity_list}
    else:
        attributes: ADMAttributes = dict()

    result: ADMDoc = {
        "version": "1.1.0",
        "data": example["content"],
        "attributes":attributes,
        "documentMetadata": get_converted_metadata(example)
    }
    return result


def save_lighttag_job_to_adm(job_data:JobResult,out_path:str,reviewed_only:bool =False,allow_overwrite=False,
                             exclude_attributes=False):
    '''
    Takes a JSON as outputted from LightTag and creates ADMS in the structure expected by FTK
    Examples that have not been seen by a human are prefixed with u_ otherwise prefixed with a_

    The output path is outpath/jobname where jobname is the name of the job
    :param job_data: The LightTag format JSON
    :param out_path:  The path to write the output to
    :param reviewed_only: If true, only reviewed data will be returned (False by default)
    :param allow_overwrite: Will write to an existing job directory if it exists (False by default)
    :param exclude_attributes: Eliminate the attributes part from the adm to be used as an input for basis 'evaluate' (False by default)
    :return:  None, writes files to disk
    '''
    job_slug = make_slug(job_data['name'])
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    job_path = os.path.join(out_path,job_slug)
    if os.path.exists(job_path) and allow_overwrite:
        pass
    else:
        os.mkdir(job_path)
    for example in job_data['examples']:
        prefix = 'u' if len(example['seen_by']) ==0 else 'a'
        adm = convert_lighttag_example_to_adm(example,reviewed_only=reviewed_only,
                                              exclude_attributes=exclude_attributes)
        adm_path = os.path.join(job_path, f"{prefix}_{example['example_id']}.adm.json")
        with open(adm_path,"w") as f:
            json.dump(adm, f, indent=2, ensure_ascii=False)



