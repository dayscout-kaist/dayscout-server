import os
import requests

ES_URL = os.environ["ES_URL"] if "ES_URL" in os.environ else "http://bap.sparcs.org:31007"
ES_URL = os.environ["ES_URL"] if "ES_URL" in os.environ else "http://localhost:9200"
ES_INDEX = "nutrient_ver_01"

def search_nutrition(text: str):
    query = {
        "query": {
            "match": {
                "name": text
            }
        }
    }
    response = requests.post(ES_URL + "/" + ES_INDEX + "/_search", json=query)
    result = response.json()
    return result["hits"]["hits"]
