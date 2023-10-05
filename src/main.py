from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile

from src.docs import TextBody, TextResponse
from src.nutrition_search import search_nutrition

# from src.barcode_search import barcode_search
from src.ocr import clova_ocr

load_dotenv()
app = FastAPI()


@app.post("/text")
async def search_from_text(body: TextBody) -> TextResponse:
    try:
        results = search_nutrition(body.text)
        return {"nutritions": results}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


# @app.post("/barcode")
# async def search_from_barcode(body: TextBody) -> TextResponse:
#     try:
#         results = search_nutrition(body.text)
#         return {"nutritions": results}
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/nutrition-facts-image")
async def search_from_nf_image(file: UploadFile):
    try:
        file_contents = await file.read()
        nut_info = clova_ocr(file_contents)
        return {"nutrition": nut_info}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
