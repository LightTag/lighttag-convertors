from adm_to_lighttag import adm_document_list_to_lighttag_suggestions
import json
import os


def get_seen_examples():
    adms = []
    for root, d, files in os.walk('/tmp/sixgill/'):
        for f in files:
            if f.endswith('adm.json'):
                adms.append(json.load(open(os.path.join(root, f))))

    seen_examples = adm_document_list_to_lighttag_suggestions(adms)
    return seen_examples


if __name__ == "__main__":
    seen_examples = get_seen_examples()
    with open('/tmp/sg_suggestions.json', 'w') as f:
        json.dump(seen_examples, f, indent=2, ensure_ascii=False)
    print("hello")

