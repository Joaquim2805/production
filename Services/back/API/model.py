
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    id: str
    password: str


class User(UserBase, table=True):
    # Spécifiez la colonne id comme clé primaire
    id: str = Field(primary_key=True)


class UserCreate(UserBase):
    pass
