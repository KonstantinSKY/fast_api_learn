from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    id: int
    role_id: int
    username: str


class UserCreate(schemas.BaseUserCreate):
    role_id: int
    username: str

