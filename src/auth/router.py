from fastapi import APIRouter
from auth.config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

router = APIRouter()

PREFIX = "/auth"
TAGS = ["Auth"]


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=PREFIX,
    tags=TAGS,
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=PREFIX,
    tags=TAGS,
)