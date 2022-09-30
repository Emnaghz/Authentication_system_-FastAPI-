from fastapi import APIRouter 

router = APIRouter()

router = APIRouter(
    prefix="/users",
    tags=["User"],
)

@router.get("/")
def hello():
    return "i am new here"