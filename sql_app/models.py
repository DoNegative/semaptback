from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    FIO = Column(String)
    email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    number_phone = Column(String)
    position_id = Column(Integer, ForeignKey("positions.id"))

    positions = relationship("Position", back_populates="owner")


class Position (Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    wage =Column(Integer)
    

    owner = relationship("User", back_populates="positions")

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
