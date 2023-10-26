import json
import re
import time
import uuid

import requests


def clova_ocr(client_id, client_secret, file_contents):
    API_URL = "https://5xcfpcnwfi.apigw.ntruss.com/custom/v1/25058/038a80468ee57106c9c2c789de5ad7a69b576c0bef74fa695e4dc7db1767d967/general"

    request_json = {
        "images": [{"format": "jpeg", "name": "good_1"}],
        "requestId": str(uuid.uuid4()),
        "version": "V2",
        "timestamp": int(round(time.time() * 1000)),
    }

    payload = {"message": json.dumps(request_json).encode("UTF-8")}
    files = [("file", file_contents)]
    headers = {"X-OCR-SECRET": client_secret}
    response = requests.request(
        "POST", API_URL, headers=headers, data=payload, files=files
    )
    result = response.json()
    with open("result.json", "w", encoding="utf-8") as make_file:
        json.dump(result, make_file, indent="\t", ensure_ascii=False)
    text = ""
    for field in result["images"][0]["fields"]:
        text += field["inferText"]

    # 총 내용량 파싱
    total_content = re.search(r"총내용량 ?([\d\.]+) ?g", text)
    # total_content = re.search(r'총내용량([\d\.]+g(?:\([\d\.]+gX\d+봉지\))?)', text)
    total_content = total_content.group(1) + "g" if total_content else None
    if total_content == None:
        total_content = re.search(r"내용량 ?([\d\.]+) ?g", text)
        total_content = total_content.group(1) + "g" if total_content else None

    per_unit = re.search(r"총 ?내용량 ?당", text)
    per_unit = "총내용량당" if per_unit else None
    print(text)

    # 단위 파싱
    if per_unit == None:
        per_unit = re.search(r"(100 ?g) ?당", text)
        per_unit = per_unit.group(1) + "당" if per_unit else None
    if per_unit == None:
        per_unit = re.search(r"내용량 ?당", text)
        per_unit = "총내용량당" if per_unit else None
    if per_unit == None:
        per_unit = re.search(r"\d+(\.\d+)?g[ )]?당", text)
        per_unit = per_unit.group(0) if per_unit else None

    # unit = re.search(r'(g|량)?당', text)
    # unit = unit.group(1) + "g" if unit else None

    # 나트륨 파싱
    sodium = re.search(r"나트륨([\d\.,]+)mg", text)
    sodium = sodium.group(1) + "mg" if sodium else None

    # 탄수화물 파싱
    carb = re.search(r"탄수화물([\d\.,]+)g", text)
    carb = carb.group(1) + "g" if carb else None

    # 당류 파싱
    sugar = re.search(r"당류([\d\.,]+)g", text)
    sugar = sugar.group(1) + "g" if sugar else None

    # 지방 파싱
    fat = re.search(r"지방([\d\.,]+)g", text)
    fat = fat.group(1) + "g" if fat else None

    # 트랜스지방 파싱
    trans_fat = re.search(r"트랜스지방([\d\.,]+)g", text)
    trans_fat = trans_fat.group(1) + "g" if trans_fat else None

    # 포화지방 파싱
    sat_fat = re.search(r"포화지방([\d\.,]+)g", text)
    sat_fat = sat_fat.group(1) + "g" if sat_fat else None

    # 콜레스테롤 파싱
    cholesterol = re.search(r"콜레스테롤([\d\.,]+)mg", text)
    cholesterol = cholesterol.group(1) + "mg" if cholesterol else None

    # 단백질 파싱
    protein = re.search(r"단백질([\d\.,]+)g", text)
    protein = protein.group(1) + "g" if protein else None

    # 칼슘 파싱
    calcium = re.search(r"칼슘([\d\.,]+)mg", text)
    calcium = calcium.group(1) + "mg" if calcium else None
    if total_content != None or carb != None:
        return {
            "총내용량": total_content,
            "단위": per_unit,
            "나트륨": sodium,
            "탄수화물": carb,
            "당류": sugar,
            "지방": fat,
            "트랜스지방": trans_fat,
            "포화지방": sat_fat,
            "콜레스테롤": cholesterol,
            "단백질": protein,
            "칼슘": calcium,
        }

    # Eng version.
    # Total Content Parsing

    serving = re.search(r"ServingSize\d+([a-zA-Z]+)\((\d+)([a-zA-Z]+)\)", text)
    per_unit = serving.group(2) if serving else None
    unit = serving.group(3) if serving else None

    total_content = re.search(r"Total?Content ?([\d\.]+) ?g", text)
    total_content = total_content.group(1) + "g" if total_content else None
    if total_content == None:
        servings_per_container = re.search(
            r"Servings ?Per ?Container(\d+)|(\d+)Servings ?Per ?Container", text
        )
        servings_per_container = (
            servings_per_container.group(1) or servings_per_container.group(2)
            if servings_per_container
            else None
        )
        total_content = servings_per_container
        total_content = (
            str(int(total_content) * int(per_unit)) if per_unit else total_content
        )

    # 단위 붙이기
    if unit != None:
        per_unit = per_unit + unit
        total_content = total_content + unit

    # Sodium Parsing
    sodium = re.search(r"Sodium([\d\.,]+)mg", text)
    sodium = sodium.group(1) + "mg" if sodium else None

    # Carbohydrate Parsing
    carb = re.search(r"Carbohydrate([\d\.,]+)g", text)
    carb = carb.group(1) + "g" if carb else None

    # Sugar Parsing
    sugar = re.search(r"Sugars([\d\.,]+)g", text)
    sugar = sugar.group(1) + "g" if sugar else None

    # Fat Parsing
    fat = re.search(r"Total ?Fat([\d\.,]+)g", text)
    fat = fat.group(1) + "g" if fat else None

    # Trans Fat Parsing
    trans_fat = re.search(r"Trans ?Fat([\d\.,]+)g", text)
    trans_fat = trans_fat.group(1) + "g" if trans_fat else None

    # Saturated Fat Parsing
    sat_fat = re.search(r"Saturated ?Fat([\d\.,]+)g", text)
    sat_fat = sat_fat.group(1) + "g" if sat_fat else None

    # Cholesterol Parsing
    cholesterol = re.search(r"Cholesterol([\d\.,]+)mg", text)
    cholesterol = cholesterol.group(1) + "mg" if cholesterol else None

    # Protein Parsing
    protein = re.search(r"Protein([\d\.,]+)g", text)
    protein = protein.group(1) + "g" if protein else None

    # Calcium Parsing
    calcium = re.search(r"Calcium([\d\.,]+)mg", text)
    calcium = calcium.group(1) + "mg" if calcium else None

    # Vitamin A Parsing
    vitamin_a = re.search(r"Vitamin A([\d\.,]+)%", text)
    vitamin_a = vitamin_a.group(1) + "%" if vitamin_a else None

    # Vitamin C Parsing
    vitamin_c = re.search(r"Vitamin C([\d\.,]+)%", text)
    vitamin_c = vitamin_c.group(1) + "%" if vitamin_c else None

    # ... (Add more as needed)

    return {
        "총내용량": total_content,
        "단위": per_unit,
        "나트륨": sodium,
        "탄수화물": carb,
        "당류": sugar,
        "지방": fat,
        "트랜스지방": trans_fat,
        "포화지방": sat_fat,
        "콜레스테롤": cholesterol,
        "단백질": protein,
        "칼슘": calcium,
    }


__all__ = ["clova_ocr"]
