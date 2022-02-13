from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from dao import RetornaSession

retorna = RetornaSession()

engine, session = retorna.retornaSession()

Base = declarative_base()

class Client(Base):
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(100), nullable=False)

Base.metadata.create_all(engine)
