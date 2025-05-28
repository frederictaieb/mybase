from fastapi import APIRouter
from .models import Item

router = APIRouter()

ITEMS = [
    {"id": 1, "name": "Test"},
    {"id": 2, "name": "Test2"},
    {"id": 3, "name": "Test3"},
]

@router.get("/items/")
def list_items() -> list[Item]:
    return ITEMS