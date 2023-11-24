import asyncio
import json
from typing import Optional

import httpx
from lxml import html
from pydantic import BaseModel

from src.models import FoodModel
from src.schemas import Nutrients


class Product(BaseModel):
    id: int
    name: str
    image_src: str
    barcode_number: int
    large_category: str
    medium_category: str
    small_category: str
    x_small_category: str


class ProductWithDetails(Product):
    display_name: str
    total_weight: Optional[float]
    nutrients: Nutrients


def multi(element, selector: str):
    return element.cssselect(selector)


def single(element, selector: str):
    return element.cssselect(selector)[0]


def text(element, selector: str):
    return element.cssselect(selector)[0].text_content()


def parse_nutrient_value(value: str) -> float:
    value = (
        value.replace(" ", "").replace("g", "").replace("kcal", "").replace("m", "e-3")
    )
    # "5e-3미만"을 0로 변환
    if "미만" in value:
        return 0
    elif not value.isdigit():
        return 0
    else:
        return float(value)


async def get_product_list(keyword: str | int) -> list[Product]:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(
            "http://www.allproductkorea.or.kr/products/info",
            params={
                "q": json.dumps({"mainKeyword": keyword, "subKeyword": ""}),
                "page": 1,
                "size": 10,
            },
        )

    document = html.fromstring(response.text)

    return [
        parse_product_info(element)
        for element in document.cssselect("div.spl_list > ul > li")
    ]


async def get_product_by_id(id: int) -> FoodModel:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(
            f"http://www.allproductkorea.or.kr/products/info/korcham/{id}"
        )

    if response.status_code == 500:
        return None
        raise Exception("Invalid product id")

    document = html.fromstring(response.text)
    info_table = single(document, ".pdv_wrap_korcham > table")

    large_category, medium_category, small_category, x_small_category = text(
        info_table, ".clsTotalNm"
    ).split(">")

    nutrient_rows = multi(document, "table.pop_list > tbody > tr")

    nutrient_dict = {
        cell[0].text_content(): parse_nutrient_value(cell[1].text_content())
        for cell in [multi(row, "td") for row in nutrient_rows]
        if len(cell) == 3
    }

    nutrients = Nutrients(
        carbohydrate=nutrient_dict.get("탄수화물"),
        protein=nutrient_dict.get("단백질"),
        fat=nutrient_dict.get("지방"),
        sugar=nutrient_dict.get("당류"),
        energy=nutrient_dict.get("열량"),
    )
    if not text(info_table, "td.originVolume").isdigit():
        return None

    return FoodModel(
        type="distribution",
        name=text(document, "h3.detail"),
        image_src=single(document, ".pdv_img > img")
        .get("src")
        .replace("250_w", "1000_w"),
        barcode_number=text(info_table, "td.gtin"),
        class_name=small_category,
        represent_name=medium_category,
        unit="abslolute",
        primary_unit="g",
        display_name=text(info_table, "td.prdNmKor"),
        total_weight=text(info_table, "td.originVolume"),
        carbohydrate=nutrients.carbohydrate,
        protein=nutrients.protein,
        fat=nutrients.fat,
        sugar=nutrients.sugar,
        energy=nutrients.energy,
    )
    # return ProductWithDetails(
    #     id=id,
    #     name=text(document, "h3.detail"),
    #     image_src=single(document, ".pdv_img > img")
    #     .get("src")
    #     .replace("250_w", "1000_w"),
    #     barcode_number=text(info_table, "td.gtin"),
    #     large_category=large_category,
    #     medium_category=medium_category,
    #     small_category=small_category,
    #     x_small_category=x_small_category,
    #     display_name=text(info_table, "td.prdNmKor"),
    #     total_weight=text(info_table, "td.originVolume"),
    #     nutrients=nutrients,
    # )


async def get_product_from_barcode(barcode_number: int):
    # Search from database first

    # If not found, search from web

    # TODO : Validate barcode number
    # if barcode_number is not valid:
    #   raise Exception("Invalid barcode number")

    product_list = await get_product_list(barcode_number)

    if len(product_list) == 0:
        raise Exception("No such barcode number")

    product_id = product_list[0].id

    return await get_product_by_id(product_id)


def parse_product_info(element) -> Product:
    product_id = element.get("data-prd-no")
    image_src = (
        element.cssselect(".spl_img > img")[0].get("src").replace("250_w", "1000_w")
    )

    name = element.cssselect(".spl_pt > strong")[0].text_content()
    barcode_number = element.cssselect(".spl_pt > em")[0].text_content()

    large_category, medium_category, small_category, x_small_category = text(
        element, ".spl_pm"
    ).split(">")

    return Product(
        id=product_id,
        name=name,
        image_src=image_src,
        barcode_number=barcode_number,
        large_category=large_category,
        medium_category=medium_category,
        small_category=small_category,
        x_small_category=x_small_category,
    )


if __name__ == "__main__":
    from pprint import pprint

    pprint(asyncio.run(get_product_list("데자와")))
    pprint(asyncio.run(get_product_from_barcode(8801097481206)))  # 데자와
    pprint(asyncio.run(get_product_by_id(100397366)))  # 데자와

    pprint(asyncio.run(get_product_from_barcode(123)))  # Invalid barcode number
    pprint(asyncio.run(get_product_by_id(123)))  # Invalid product id
