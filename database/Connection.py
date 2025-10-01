#Responsavel por controlar a abertura e fechamento de sessão configurar driver entre outros
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from .Base import Base

class Connection:
    
    def __init__(self):
        self.engine = create_engine('sqlite:///meu_banco_de_dados.db', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
        
    def getSession(self):
        return self.Session()
    
    def save(self,model=None):
        if(model is None):
            return None

        Session = self.getSession()
        try:
            Session.add(model)
            Session.commit()
        finally:
            Session.close()
    
    def checkIfExists(self,model,value):
        session = self.getSession()
        try:
            return session.query(exists().where(model == value)).scalar()
        except Exception as e:
            raise Exception("Error check if exists")