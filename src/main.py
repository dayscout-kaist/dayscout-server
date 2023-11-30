from fastapi import FastAPI

from src.api import allproductkorea, auth, food, nutrient, post, report, review, tag

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(food.router, prefix="/food", tags=["food"])
app.include_router(report.router, prefix="/report", tags=["report"])
app.include_router(review.router, prefix="/review", tags=["review"])
app.include_router(nutrient.router, prefix="/nutrient", tags=["nutrient"])
app.include_router(tag.router, prefix="/tag", tags=["tag"])
app.include_router(post.router, prefix="/post", tags=["post"])
app.include_router(
    allproductkorea.router, prefix="/allproductkorea", tags=["allproductkorea"]
)
