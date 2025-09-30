from sqlalchemy import Column, Integer, String

from database.Base import Base

class User(Base):
    __tablename__ = "db_users"
    id = Column(Integer,primary_key=True)
    id_telegram = Column(String,nullable=False)
    
    pass