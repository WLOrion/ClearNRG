from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus

import os
# Carregar as variáveis de ambiente
load_dotenv()

# Configurar a URL do banco de dados a partir do arquivo .env
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
database = os.getenv("MYSQL_DATABASE")
user_encoded = quote_plus(user)
password_encoded = quote_plus(password)


db_url = f"mysql+mysqlconnector://{user_encoded}:{password_encoded}@{host}:{port}/{database}"

# Configurar o motor de conexão com o banco de dados
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função para executar uma query SQL genérica
def execute_query(db, query):
    result = db.execute(text(query))
    return result.fetchall()
