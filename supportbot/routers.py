from fastapi import APIRouter
from .resources import views

router = APIRouter()

# Routers
router.include_router(views.router)