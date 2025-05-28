from sqlmodel import SQLModel, Field

class Item(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: str