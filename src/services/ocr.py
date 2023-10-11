import json
import re
import time
import uuid

import requests

from src.schemas import AbsoluteUnit, FoodContent, Nutrients, SingleUnit, TotalUnit
from src.settings import settings


async def parse_nutrients_from_image(image: bytes) -> FoodContent:
    request_json = {
        "images": [{"format": "jpeg", "name": "good_1"}],
        "requestId": str(uuid.uuid4()),
        "version": "V2",
        "timestamp": int(time.time() * 1000),
    }

    result = requests.request(
        method="POST",
        url=settings.CLOVA_API_URL,
        headers={"X-OCR-SECRET": settings.CLOVA_CLIENT_SECRET},
        data={"message": json.dumps(request_json).encode("UTF-8")},
        files=[("file", image)],
    ).json()

    text = "".join([field["inferText"] for field in result["images"][0]["fields"]])

    # 총 내용량 파싱
    total_content = re.search(r"총내용량 ?([\d.]+) ?g", text)
    # total_content = re.search(r'총내용량([\d\.]+g(?:\([\d\.]+gX\d+봉지\))?)', text)
    total_content = total_content.group(1) + "g" if total_content else None
    if total_content == None:
        total_content = re.search(r"내용량 ?([\d.]+) ?g", text)
        total_content = total_content.group(1) + "g" if total_content else None

    # 단위 파싱
    per_unit = re.search(r"총 ?내용량 ?당", text)
    per_unit = TotalUnit() if per_unit else None

    if per_unit is None:
        per_unit = re.search(r"(100 ?g) ?당", text)
        per_unit = AbsoluteUnit() if per_unit else None
    if per_unit is None:
        per_unit = re.search(r"내용량 ?당", text)
        per_unit = TotalUnit() if per_unit else None
    if per_unit is None:
        per_unit = re.search(r"\d+(\.\d+)?g[ )]?당", text)
        per_unit = per_unit.group(0) if per_unit else None

    # unit = re.search(r'(g|량)?당', text)
    # unit = unit.group(1) + "g" if unit else None

    # # 나트륨 파싱
    # sodium = re.search(r"나트륨([\d\.,]+)mg", text)
    # sodium = sodium.group(1) + "mg" if sodium else None

    # 탄수화물 파싱
    carb = re.search(r"탄수화물([\d.,]+)g", text)
    carb = carb.group(1) + "g" if carb else None

    # 당류 파싱
    sugar = re.search(r"당류([\d.,]+)g", text)
    sugar = sugar.group(1) + "g" if sugar else None

    # 지방 파싱
    fat = re.search(r"지방([\d.,]+)g", text)
    fat = fat.group(1) + "g" if fat else None

    # # 트랜스지방 파싱
    # trans_fat = re.search(r"트랜스지방([\d\.,]+)g", text)
    # trans_fat = trans_fat.group(1) + "g" if trans_fat else None

    # # 포화지방 파싱
    # sat_fat = re.search(r"포화지방([\d\.,]+)g", text)
    # sat_fat = sat_fat.group(1) + "g" if sat_fat else None

    # # 콜레스테롤 파싱
    # cholesterol = re.search(r"콜레스테롤([\d\.,]+)mg", text)
    # cholesterol = cholesterol.group(1) + "mg" if cholesterol else None

    # 단백질 파싱
    protein = re.search(r"단백질([\d.,]+)g", text)
    protein = protein.group(1) + "g" if protein else None

    # # 칼슘 파싱
    # calcium = re.search(r"칼슘([\d\.,]+)mg", text)
    # calcium = calcium.group(1) + "mg" if calcium else None

    return FoodContent(
        totalWeight=total_content,
        unit=per_unit,
        primaryUnit="g",
        nutrients=Nutrients(
            carb=carb,
            sugar=sugar,
            fat=fat,
            protein=protein,
        ),
    )