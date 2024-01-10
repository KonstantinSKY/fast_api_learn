from fastapi import APIRouter, Depends

from auth.config import fastapi_users
from auth.models import User

router = APIRouter(
    tags=["LandingPage"]
)


@router.get("/", operation_id="getHello")
def get_hello():
    return "Hello World!"


current_user = fastapi_users.current_user()


@router.get("/protected-route", tags=["ProtectedLanding"])
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@router.get("/unprotected-route")
def unprotected_route():
    return f"Hello, Anonym"

#
# @app.get("/users/{user_id}", response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in f_users if user.get("id") == user_id]
#
