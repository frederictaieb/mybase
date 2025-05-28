from fastapi import APIRouter
from .models import Item

router = APIRouter()

@router.get("/items/")
def list_items():
    return [{"id": 1, "name": "Test"}]
