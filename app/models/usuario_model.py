from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Usuario(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    # Definindo  da tabela.
    id = Column(Integer, primary_key= True, autoincrement= True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind = db)