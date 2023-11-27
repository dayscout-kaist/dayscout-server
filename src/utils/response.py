from humps import camelize
from pydantic import BaseModel


class RequestModel(BaseModel):
    class Config:
        alias_generator = camelize
        populate_by_name = True
        orm_mode = True


class ResponseModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
        orm_mode = True
