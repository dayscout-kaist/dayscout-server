from dotenv import load_dotenv
from fastapi import Body, FastAPI, File, UploadFile
from pydantic import BaseModel

from src.nutrition_search import search_nutrition
from src.ocr import clova_ocr

class TextBody(BaseModel):
    text: str = ""

load_dotenv()
app = FastAPI()

@app.post("/text")
async def search_from_text(body: TextBody):
    try:
        results = search_nutrition(body.text)
        return {"results": results}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@app.post("/nutrition-facts-image")
async def search_from_nf_image(file: UploadFile):
    file_contents = await file.read()
    client_id = client.client_id
    client_secret = client.client_secret
    nut_info = ocr.clova_ocr(client_id, client_secret, file_contents)
    return {"status": "success", "nut_info": nut_info}
