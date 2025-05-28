from sqlmodel import Session, select
from typing import List, Optional

from .models import Item, ItemCreate, ItemRead

def get_item(session: Session, item_id: int) -> Optional[Item]:
    """Récupère un item par son ID"""
    return session.get(Item, item_id)

def get_items(session: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """Récupère une liste d'items avec pagination"""
    statement = select(Item).offset(skip).limit(limit)
    return session.exec(statement).all()

def create_item(session: Session, item: ItemCreate) -> Item:
    """Crée un nouvel item"""
    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def update_item(session: Session, item_id: int, item_data: ItemCreate) -> Optional[Item]:
    """Met à jour un item existant"""
    db_item = get_item(session, item_id)
    if not db_item:
        return None
        
    # Mettre à jour les attributs
    item_data_dict = item_data.dict(exclude_unset=True)
    for key, value in item_data_dict.items():
        setattr(db_item, key, value)
    
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def delete_item(session: Session, item_id: int) -> bool:
    """Supprime un item par son ID"""
    db_item = get_item(session, item_id)
    if not db_item:
        return False
        
    session.delete(db_item)
    session.commit()
    return True
