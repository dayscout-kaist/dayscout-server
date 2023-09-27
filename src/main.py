import importlib.util

from fastapi import Body, FastAPI, File, UploadFile

spec = importlib.util.spec_from_file_location("client", "src/client.py")
client = importlib.util.module_from_spec(spec)
spec.loader.exec_module(client)

spec = importlib.util.spec_from_file_location("ocr", "src/ocr.py")
ocr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ocr)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/nutrition-facts")
async def upload_image(file: UploadFile):
    # return {"file": file}
    print("hi")
    file_contents = await file.read()
    client_id = client.client_id
    client_secret = client.client_secret
    nut_info = ocr.clova_ocr(client_id, client_secret, file_contents)
    print(nut_info)

    return {"status": "success", "nut_info": nut_info}
