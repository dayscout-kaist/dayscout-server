from pydantic import BaseModel


class Nutrition(BaseModel):
    name: str | None
    weight: str | None
    nutrient_reference_weight: str | None
    energy: float | None
    protein: float | None
    fat: float | None
    carbohydrate: float | None
    sugar: float | None
    manufacturer: str | None


class TextBody(BaseModel):
    text: str = ""


class TextResponse(BaseModel):
    nutritions: list[Nutrition] = []


class NFImageResponse(BaseModel):
    nutrition: Nutrition
