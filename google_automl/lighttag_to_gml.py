from typing import List, Dict

from google_automl.type_definitions import GML_JSONLExample, GML_Annotation
from google_automl.type_definitions.gml_annotation import (
    GML_AnnotationTextExtraction,
    GML_AnnotationTextSegment,
)
from lighttag.type_definitions.lighttag_job import JobResult
from lighttag.type_definitions.lighttag_result_types import LTExample, Annotation


class NotGMLPDFExample(Exception):
    pass


def has_gml_metadata(example: LTExample) -> bool:
    """
    Checks if the example has the GML metadata required
    :param example:
    :return: boolean
    """
    metadata = example["metadata"]
    return metadata.get("gml", None) is not None


def lighttag_annotation_to_gml_annotation(lt_anno: Annotation) -> GML_Annotation:
    """
    Converts a LightTag annotation to a GML format annotation
    :param lt_anno:
    :return:
    """
    textSegment = GML_AnnotationTextSegment(
        startOffset=str(lt_anno["start"]), endOffset=str(lt_anno["end"])
    )
    textExtraction = GML_AnnotationTextExtraction(textSegment=textSegment)
    result = GML_Annotation(displayName=lt_anno["tag"], textExtraction=textExtraction)
    return result


def lighttag_example_to_gml(example: LTExample) -> GML_JSONLExample:
    """
    Converts a LightTag example as received from LightTag servers into the JSONL format that google expects for PDFs.
    This function checks that the example has the GML data on it (all the pdf metadata) and raises an Exception of it doesn't


    :param example: A LightTag example
    :return: A GML_JSONLExample object
    """
    if not has_gml_metadata(example):
        raise NotGMLPDFExample(
            "This example doesn't have the metadata to be processed by Google AutoML. The GML object is missing"
        )

    gml: GML_JSONLExample = example["metadata"]["gml"]
    # Restore the text, we moved it off the gml object when uploading to LightTag
    gml["document"]["documentText"]["content"] = example["content"]
    gml_annotations: List[GML_Annotation] = list(
        map(lighttag_annotation_to_gml_annotation, example["annotations"])
    )
    gml["annotations"] = gml_annotations
    return gml

def lighttag_job_to_gml_dict(job:JobResult) ->Dict[str,GML_JSONLExample]:
    '''
    Gets the LightTag result file (what you download/retreive from the UI) and converts it into a dictionary
    whose values are the GML objects and keys are the original JSONL filename.

    We return a dict, so that you can easily iterate over dict.items() and write the object to a trackable filename
    :param job: The LightTag JOB
    :return: A dictionary
    '''
    result :Dict[str,GML_JSONLExample] = {}
    for example in job['examples']:
        filename = example['metadata'].get('jsonl_filename',None)
        if filename is None:
            raise NotGMLPDFExample("One of the examples does not have the original filename in it's metadata. This is probably not GML data")
        result[filename] = lighttag_example_to_gml(example)
    return result



