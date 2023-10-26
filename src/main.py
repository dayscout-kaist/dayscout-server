import importlib.util

from fastapi import Depends, FastAPI, HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.client import *

spec = importlib.util.spec_from_file_location("userDB", "src/userDB.py")
userDB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(userDB)

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
    file_contents = await file.read()
    client_id = client.client_id
    client_secret = client.client_secret
    nut_info = ocr.clova_ocr(client_id, client_secret, file_contents)
    print(nut_info)

    return {"status": "success", "nut_info": nut_info}


init = userDB.init_db()


def get_db():
    db = userDB.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(
    username: str, email: str, password: str, db: Session = Depends(get_db)
):
    user = userDB.User(username=username, email=email, hashed_password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(userDB.User).filter(userDB.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
