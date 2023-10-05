import os

import requests

ES_URL = (
    os.environ["ES_URL"] if "ES_URL" in os.environ else "http://bap.sparcs.org:31007"
)
ES_URL = os.environ["ES_URL"] if "ES_URL" in os.environ else "http://localhost:9200"
ES_INDEX = "nutrient_ver_01"


def search_nutrition(text: str):
    query = {"query": {"match": {"name": text}}}
    response = requests.post(ES_URL + "/" + ES_INDEX + "/_search", json=query)
    result = response.json()
    return list(
        map(
            lambda x: {
                "name": x["_source"]["name"],
                "weight": x["_source"]["weight"],
                "nutrient_reference_weight": x["_source"]["nutrient_reference_weight"],
                "energy": x["_source"]["energy"],
                "protein": x["_source"]["protein"],
                "fat": x["_source"]["fat"],
                "carbohydrate": x["_source"]["carbohydrate"],
                "sugar": x["_source"]["sugar"],
                "manufacturer": x["_source"]["manufacturer"],
            },
            result["hits"]["hits"],
        )
    )
