from typing import Callable, List

from type_definitions.adm_types import ADMDoc, Entity
from type_definitions.lighttag_suggestion_types import LTSuggestionInput


def default_example_id_fn(doc: ADMDoc) -> str:
    # TODO @Nadav, I think you changed the type of the metadata to be a list ?
    return doc["documentMetadata"]["lighttag_example_id"]


def default_tag_name_extractor(entity: Entity) -> str:

    return entity["type"]


def adm_doc_to_lighttag_suggetions(
    doc: ADMDoc,
    example_id_fn: Callable[[ADMDoc], str] = default_example_id_fn,
    lighttag_tag_name_extractor: Callable[[Entity], str] = default_tag_name_extractor,
) -> List[LTSuggestionInput]:
    """

    :param doc:  An ADMDoc container the predictions from Rosette
    :param example_id_fn: A function that extracts the LightTag example_id from the adm doc
    :param lighttag_tag_name_extractor: A function that converts the entity type into the name of the tag in LightTag
    :return: LightTag suggestions to be sent to LightTag
    """
    example_id = example_id_fn(doc)
    predictied_entities = doc["attributes"]["entities"]["items"]
    suggestions: List[LTSuggestionInput] = []
    for adm_prediction in predictied_entities:
        tag = lighttag_tag_name_extractor(adm_prediction)
        mention = adm_prediction["mentions"][0]
        suggestion: LTSuggestionInput = {
            "tag": tag,
            "example_id": example_id,
            "start": mention["startOffset"],
            "end": mention["endOffset"],
            "text": mention["normalized"],
        }
        suggestions.append(suggestion)
    return suggestions


def adm_document_list_to_lighttag_suggestions(
    docs: List[ADMDoc],
    example_id_fn: Callable[[ADMDoc], str] = default_example_id_fn,
    lighttag_tag_name_extractor: Callable[[Entity], str] = default_tag_name_extractor,
):
    """

    :param docs: A list of ADM Docs
    :param example_id_fn:
    :param lighttag_tag_name_extractor:
    :return: LightTag suggestions to be sent to LightTag
    """
    suggestions: List[LTSuggestionInput] = []
    for doc in docs:
        suggestions += adm_doc_to_lighttag_suggetions(
            doc,
            example_id_fn=example_id_fn,
            lighttag_tag_name_extractor=lighttag_tag_name_extractor,
        )
    return suggestions
