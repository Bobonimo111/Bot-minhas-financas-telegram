from sqlalchemy import  Column, Integer, String
import Base


# Tabela onde ficaram dados de contas
class Balanco(Base):
    __tablename__ = "Balanco"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
