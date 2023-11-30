import pandas as pd
import requests
from tqdm import tqdm

# 엑셀 파일 경로
excel_path = "initialDB.xlsx"

# FastAPI 엔드포인트
api_endpoint = "https://dayscout.sparcsandbox.com/food/create"


def generate_food_data():
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_path)

    # 엑셀 파일의 각 행을 반복하여 API 호출
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        food_data = {
            "name": row["식품명"],
            "representName": row["대표식품명"],
            "className": str(row["식품중분류명"]),
            "totalWeight": float(row["식품중량"]),
            "primaryUnit": "g",
            "unit": "absolute",
            "carbohydrate": row["탄수화물(g)"],
            "protein": row["단백질(g)"],
            "fat": row["지방(g)"],
            "sugar": None if row["당류(g)"] == "해당없음" else row["당류(g)"],
            "energy": row["에너지(kcal)"],
            "type": "general",
        }

        # 헤더에 'Content-Type'을 'application/json'으로 설정
        headers = {"Content-Type": "application/json"}

        response = requests.post(api_endpoint, json=food_data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to add data for {row['식품명']}: {response.text}")


if __name__ == "__main__":
    generate_food_data()
