from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .Base import Base

class User(Base):
    __tablename__ = "db_user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    id_telegram = Column(String,nullable=False,unique=True)
    nome = Column(String,nullable=True)
    
    gastos = relationship("Gasto",back_populates="user")