from sqlmodel import SQLModel, Field
from typing import Optional

class ItemBase(SQLModel):
    """Modèle de base pour les items"""
    name: str
    description: Optional[str] = None
    
class Item(ItemBase, table=True):
    """Modèle Item pour la base de données"""
    __tablename__ = "items"
    
    id: Optional[int] = Field(default=None, primary_key=True)

class ItemCreate(ItemBase):
    """Modèle pour la création d'un item"""
    pass

class ItemRead(ItemBase):
    """Modèle pour la lecture d'un item"""
    id: int