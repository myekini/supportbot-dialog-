from fastapi import APIRouter
from .models import Placeholder
router = APIRouter(
    prefix="/supportbot",
    tags=["supportbot"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def srscore(placeholder:Placeholder):
    """calculate social reputations score"""
    print(placeholder)
    return {"message": "HEllO FASTAPI"}



