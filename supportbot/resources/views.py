from fastapi import APIRouter



router = APIRouter(
    prefix="/supportbot",
    tags=["srscore"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def srscore():
    """calculate social reputations score"""

    return {"message": "HEllO FASTAPI"}



