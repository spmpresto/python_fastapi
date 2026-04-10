from datetime import date
from typing import Optional, List
from fastapi import Query
from pydantic import BaseModel, ConfigDict


# class SHotel(BaseModel):
#     address: str
#     name: str
#     stars: int
#
#     class Config:
#         from_attributes = True

class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)


class SHotelInfo(SHotel):
    rooms_left: int

    # class Config:
    #     from_attributes = True
    model_config = ConfigDict(from_attributes=True)

class SHotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars