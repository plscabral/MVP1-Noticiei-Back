import os
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# importando os elementos definidos no modelo
from entities.base import Base
from entities.user import User
from entities.term import Term
from entities.user_term import UserTerm

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_folder = "database"
db_url = 'sqlite:///database/db.sqlite3'

# Verifique se a pasta existe. Se não existir, crie-a.
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)