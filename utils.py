from typing import List, Callable, Optional
import re,unicodedata
from type_definitions.lighttag_result_types import Example, Annotation

def filter_predicate_factory(reviewed_only:bool) -> Callable[[Annotation],bool]:

    if not reviewed_only:
        def predicate(anno: Annotation):
            return anno['correct'] is not False and anno['start'] is not None
        return predicate
    else:
        def predicate(anno:Annotation):
            return anno['correct'] is True and anno['start'] is not None
    return predicate


def sort_example_annotations(example: Example,reviewed_only:bool=False) -> Example:
    filter_predicate = filter_predicate_factory(reviewed_only)
    not_incorrect_annotations = filter(
        filter_predicate, example["annotations"]
    )
    example["annotations"] = sorted(not_incorrect_annotations, key=lambda x: x["start"])
    return example


def check_annotations_have_conflicts(example: Example) -> bool:
    example = sort_example_annotations(example)
    annotations = example["annotations"]
    max_end = 0
    for annotation in annotations:
        if annotation["start"] < max_end:
            # if the next annotation in a sorted list starts before the longest end we've seen then we have a conflict
            # eg [0,10],[5,11]
            #
            return True
        else:
            max_end = annotation["end"]
    return False

def make_slug(s:str)->str:
    slug = unicodedata.normalize('NFKD', s).lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug

