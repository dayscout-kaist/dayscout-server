from typing import List

from fastapi import APIRouter, FastAPI, HTTPException

from src.schemas.user import User, UserCreate
from src.services.orm import create_user_db, get_user_db, get_users_db

router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    return create_user_db(user)


@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10):
    return get_users_db(skip, limit)


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = get_user_db(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
