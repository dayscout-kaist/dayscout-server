from elasticsearch import AsyncElasticsearch
from src.schemas import AbsoluteUnit, FoodContent, FoodDetail, Nutrients, PrimaryUnit
from src.settings import settings

es = AsyncElasticsearch(hosts=settings.ES_URL)


def aggregate_nutrition(food_item: dict) -> FoodDetail:
    nutrients = Nutrients(
        fat=food_item["fat"],
        carbohydrate=food_item["carbohydrate"],
        sugar=food_item["sugar"],
        energy=food_item["energy"],
        protein=food_item["protein"],
    )

    food_content = FoodContent(
        total_weight=food_item["nutrient_reference_weight"],
        unit=AbsoluteUnit(),
        primary_unit=PrimaryUnit[food_item["weight_unit"]],
        nutrients=nutrients,
    )

    return FoodDetail(
        name=food_item["name"],
        category="todo",
        manufacturer=food_item["manufacturer"],
        content=food_content,
    )


async def search_food_by_text(text: str) -> list[FoodDetail]:
    results = await es.search(
        index=settings.ES_INDEX,
        body={"query": {"match": {"text_for_search": text}}},
    )

    hits = results["hits"]["hits"]

    return [aggregate_nutrition(item["_source"]) for item in hits]
