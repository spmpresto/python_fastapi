from datetime import date

from fastapi import APIRouter, Request, Depends, BackgroundTasks
from pydantic import parse_obj_as, TypeAdapter

from fastapi_versioning import version
from app.tasks.tasks import send_booking_confirmation_email
from app.bookings.dao import BookingDAO
from app.bookings.schemes import SBooking, SBookingInfo, SNewBooking
from app.exceptions import RoomCannotBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Booking"],
)

@router.get("")
@version(1)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    return await BookingDAO.find_all_with_images(user_id=user.id)

@router.post("")
@version(2)
async def add_booking(
    #booking: SNewBooking,
    room_id: int, date_from: date, date_to: date,
    background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):

    booking = await BookingDAO.add(
        user.id,
        room_id,
        date_from,
        date_to,
    )
    #print(booking)
    if not booking:
        raise RoomCannotBeBookedException

    ### deprecated ###
    booking = parse_obj_as(SBooking, booking).dict()
    ### deprecated ###
    booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()

    # Celery
    # send_booking_confirmation_email.delay(booking, user.email)
    # Background Tasks - build in FastAPI
    #background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
    return booking

@router.delete("/{booking_id}")
@version(1)
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)

