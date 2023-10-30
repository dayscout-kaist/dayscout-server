from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def search_by_text():
    return {}


@router.post("/login")
async def login():
    return {}


@router.get("/logout")
async def logout():
    return {}


@router.post("/register")
async def logout():
    return {}
