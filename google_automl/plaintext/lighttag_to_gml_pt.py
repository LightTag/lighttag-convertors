from typing import List, Dict

from google_automl.plaintext.type_definitions import GML_PT_Annotation, GML_PT_TextSegment, GML_PT_TextExtraction, \
    GML_PT_JSONL
from lighttag.conflict_resolver import resolve_annotation_conflicts
from lighttag.type_definitions.lighttag_job import JobResult
from lighttag.type_definitions.lighttag_result_types import Annotation, LTExample


def lighttag_annotation_to_gml_annotation(lt_anno: Annotation) -> GML_PT_Annotation:
    """
    Converts a LightTag annotation to a GML format annotation
    :param lt_anno:
    :return:
    """
    textSegment = GML_PT_TextSegment(
        start_offset=str(lt_anno["start"]), end_offset=str(lt_anno["end"])
    )
    textExtraction = GML_PT_TextExtraction(text_segment=textSegment)
    result = GML_PT_Annotation(display_name=lt_anno["tag"], text_extraction=textExtraction)
    return result


def lighttag_example_to_gml(example: LTExample) -> GML_PT_JSONL:
    """
    Converts a LightTag example as received from LightTag servers into the JSONL format that google expects for PDFs.
    This function checks that the example has the GML data on it (all the pdf metadata) and raises an Exception of it doesn't


    :param example: A LightTag example
    :return: A GML_JSONLExample object
    """

    content = example["content"]
    resolved_lt_annotations = resolve_annotation_conflicts(example['annotations'])
    gml_annotations: List[GML_PT_Annotation] = list(
        map(lighttag_annotation_to_gml_annotation, resolved_lt_annotations)
    )
    result =  GML_PT_JSONL(annotations=gml_annotations,text_snippet={'content':content})
    return result

def lighttag_job_to_pt_gml_dict(job:JobResult) ->Dict[str, GML_PT_JSONL]:
    '''
    Gets the LightTag result file (what you download/retreive from the UI) and converts it into a dictionary
    whose values are the GML objects and keys are the original JSONL filename.

    We return a dict, so that you can easily iterate over dict.items() and write the object to a trackable filename
    :param job: The LightTag JOB
    :return: A dictionary
    '''
    result :Dict[str, GML_PT_JSONL] = {}
    for example in job['examples']:
        result[f"{example['example_id']}.jsonl"] = lighttag_example_to_gml(example)
    return result



