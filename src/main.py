from src.ocr import clova_ocr
from fastapi import Body, FastAPI, File, UploadFile

app = FastAPI()

@app.post("/nutrition-facts")
async def upload_image(file: UploadFile):
    file_contents = await file.read()
    client_id = client.client_id
    client_secret = client.client_secret
    nut_info = ocr.clova_ocr(client_id, client_secret, file_contents)
    return {"status": "success", "nut_info": nut_info}
