from pydantic import BaseModel
from . import models

class PositionBase(BaseModel):
    name: str
    wage: int
    @staticmethod
    def func(position: models.Position):
        return PositionBase(name = position.name, wage= position.wage)
        

class PositionCreate(PositionBase):
    pass


class Position(PositionCreate):
    id: int

    class Config:
        orm_mode = True


class AdminBase(BaseModel):
    email: str


class AdminCreate(AdminBase):
    password: str

class Admin(AdminCreate):
    id:int

class User(BaseModel):
    id:int
    FIO: str
    email: str
    number_phone: str
    position: PositionBase
    position_id: int 
    
    class Config:
        orm_mode = True

class UserPut(BaseModel):
    FIO: str
    email: str
    number_phone: str
    position_id: int

    class Config:
        orm_mode = True


