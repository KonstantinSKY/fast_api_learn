from fastapi import APIRouter

router = APIRouter(
    tags=["LandingPage"]
)


@router.get("/", operation_id="getHello")
def get_hello():
    return "Hello World!"
