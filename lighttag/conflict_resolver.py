from typing import List, Optional
import warnings
from typing_extensions import TypedDict

from lighttag.type_definitions.lighttag_result_types import Annotation


class Span(TypedDict):
    start :int
    end:int
def overlaps(a:Span,b:Span):
    if a['end'] <b['start'] or b['end'] <a['start']:
        return False
    else:
        return True
class ConflictGroup:
    def __init__(self):
        self.annotations : List[Annotation] =[]
        self.min_start : Optional[int] = None
        self.max_end: Optional[int] = None
    def add_annotation(self,annotation:Annotation):
        if self.min_start is None:
            self.min_start = annotation['start']
            self.max_end = annotation['end']
        else:
            self.min_start = min(self.min_start,annotation['start'])
            self.max_end = max(self.max_end,annotation['end'])
        self.annotations.append(annotation)
    @property
    def is_empty(self):
        return len(self.annotations) ==0
    def contains(self,annotation:Annotation):
        if self.min_start is None:
            return False
        a = annotation
        b = {'start':self.min_start,'end':self.max_end}
        return overlaps(a,b)
    def resolve(self)->Annotation:
        if len(self.annotations) ==0:
            raise Exception("Can't resolve empty conflict group")
        elif len(self.annotations)==1:
            return self.annotations[0]
        else:
            #return the annotation with the most votes, if it's a tie return the first annotation with the longest span
            sorted_annotations = sorted(self.annotations,key=lambda anno:(-1*len(anno['annotated_by']),-1*(anno['end']-anno['start'])))
            keep = sorted_annotations[0]
            reject = sorted_annotations[1:]
            reject_message = '\n'.join(map(str,reject))
            warnings.warn(f"Conflicts detected in example {self.annotations[0]['example_id']}. \n we kept {keep} and removed {reject_message}")
            return sorted_annotations[0]





def resolve_annotation_conflicts(annotations:List[Annotation])->List[Annotation]:
    if len(annotations)==0:
        return annotations
    conflict_groups  :List[ConflictGroup] =[]
    current_group :ConflictGroup = ConflictGroup()
    current_group.add_annotation(annotations[0])
    for annotation in annotations[1:]:
        if  current_group.contains(annotation):
            current_group.add_annotation(annotation)
        else:
            conflict_groups.append(current_group)
            current_group=ConflictGroup()
            current_group.add_annotation(annotation)
    if len(current_group.annotations) >0:
        # If we have a group that is not in the list
        conflict_groups.append(current_group)
    return [group.resolve() for group in conflict_groups]




