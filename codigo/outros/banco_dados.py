from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Cliente(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(255))

engine = create_engine("")

