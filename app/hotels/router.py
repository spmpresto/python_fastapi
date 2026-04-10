import asyncio
from datetime import date, datetime, timedelta

from pydantic import parse_obj_as

from fastapi import APIRouter, Request, Depends
from typing import Optional, List
from fastapi import Query

from fastapi_cache.decorator import cache


from app.hotels.dao import HotelsDAO
from app.hotels.schemes import SHotelsSearchArgs, SHotel, SHotelInfo

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)


@router.get("")
async def get_hotels(
        search_args: SHotelsSearchArgs = Depends()
) -> list[SHotel]:
    return search_args


@router.get("/{location}")
@cache(expire=20)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SHotelInfo]:
    await asyncio.sleep(1)
    hotels = await HotelsDAO.find_all(location, date_from, date_to)
    #hotels_json = parse_obj_as(List[SHotelInfo],hotels)
    return hotels


@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(
    hotel_id: int,
) -> Optional[SHotel]:
    return await HotelsDAO.find_one_or_none(id=hotel_id)