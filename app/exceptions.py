from fastapi import HTTPException, status

class BookingException(HTTPException): # <-- наследуемся от HTTPException,который наследован от Exception
    status_code = 500 # <-- задаем значения по умолчанию
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(BookingException): # <-- обязательно наследуемся от нашего класса
    status_code=status.HTTP_409_CONFLICT
    detail="User already exists"

# UserAlreadyExistsException = HTTPException(
#     status_code=status.HTTP_409_CONFLICT,
#     detail="User already exists",
# )

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect Email or Password",
)



TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired",
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token missing"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect token format"
)

UserIsNotPresentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED
)

RoomCannotBeBookedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="There are no free rooms left"
)