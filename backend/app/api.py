from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from .models import Item, ItemCreate, ItemRead
from .database import get_session
from . import crud

router = APIRouter()

@router.get("/items/", response_model=List[ItemRead])
def list_items(
    skip: int = 0, 
    limit: int = 100, 
    session: Session = Depends(get_session)
):
    """Récupère la liste des items"""
    items = crud.get_items(session, skip=skip, limit=limit)
    return items

@router.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: int, session: Session = Depends(get_session)):
    """Récupère un item par son ID"""
    db_item = crud.get_item(session, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.post("/items/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, session: Session = Depends(get_session)):
    """Crée un nouvel item"""
    return crud.create_item(session, item)

@router.put("/items/{item_id}", response_model=ItemRead)
def update_item(item_id: int, item: ItemCreate, session: Session = Depends(get_session)):
    """Met à jour un item existant"""
    db_item = crud.update_item(session, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, session: Session = Depends(get_session)):
    """Supprime un item"""
    success = crud.delete_item(session, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return None