from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

from .fields import Id


class Todo(BaseModel):

    id: Id = Field(default_factory=Id, alias='_id')
    name: str = Field(...)

    class Config:

        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'name': 'Buy anything'
            }
        }


class UpdateTodo(BaseModel):

    name: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Buy anything"
            }
        }
