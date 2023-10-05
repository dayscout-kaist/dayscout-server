import os

import requests

ES_URL = (
    os.environ["ES_URL"] if "ES_URL" in os.environ else "http://bap.sparcs.org:31007"
)
ES_INDEX = "nutrient_ver_02"


def search_nutrition(text: str):
    query = {"query": {"match": {"text_for_search": text}}}
    response = requests.post(ES_URL + "/" + ES_INDEX + "/_search", json=query)
    result = response.json()
    return list(
        map(
            lambda x: {
                "name": x["_source"]["name"],
                "category": "todo",
                "manufacturer": x["_source"]["manufacturer"],
                "content": {
                    "totalWeight": x["_source"]["nutrient_reference_weight"],
                    "unit": {
                        "type": "absolute",
                        "totalWeight": x["_source"]["weight"],
                    },
                    "primaryUnit": x["_source"]["weight_unit"],
                    "nutrients": {
                        "fat": x["_source"]["fat"],
                        "carbohydrate": x["_source"]["carbohydrate"],
                        "sugar": x["_source"]["sugar"],
                        "energy": x["_source"]["energy"],
                        "protein": x["_source"]["protein"],
                    },
                },
            },
            result["hits"]["hits"],
        )
    )
