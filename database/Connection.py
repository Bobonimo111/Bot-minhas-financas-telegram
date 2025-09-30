#Responsavel por controlar a abertura e fechamento de sessão configurar driver entre outros
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.Base import Base

class Connection:
    
    def __init__(self):
        self.engine = create_engine('sqlite:///meu_banco_de_dados.db', echo=True)
        Base.metadata.create_all(self.engine)
        
    def save(self,model=None):
        if(model is None):
            return None
        
        Session = sessionmaker(bind=self.engine)
        Session = Session()
        Session.add(model)
        Session.commit()
        
    
