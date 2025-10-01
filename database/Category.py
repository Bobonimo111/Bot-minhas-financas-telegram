from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship
from .Base import Base

class Category(Base):
    
    __tablename__ ="db_category"
    
    id = Column(Integer,name="id",primary_key=True,autoincrement=True)
    nome = Column(String,name="name",nullable=False)
    
    gastos = relationship("Gasto",back_populates="category")