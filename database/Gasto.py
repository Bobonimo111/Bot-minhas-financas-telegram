from sqlalchemy import  Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base 
from .Category import Category


# Tabela onde ficaram dados de contas
class Gasto(Base):
    __tablename__ = "db_gasto"
    id = Column(Integer, primary_key=True)
    valor = Column(String)
    local = Column(String)

    user_id = Column(Integer,ForeignKey("db_user.id"))
    category_id = Column(Integer,ForeignKey("db_category.id"))
    
    user = relationship("User",back_populates="gastos")
    category = relationship("Category",back_populates="gastos")
   