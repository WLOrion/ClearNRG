from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db, execute_query, engine
from .models import Base
from .scripts.inserir_estados import inserir_estados

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    inserir_estados()
    # carregar_cidades()
    # carregar_dados_solares()
    # carregar_dados_eolicos()

@app.get("/")
def read_root():
    return {"message": "FastAPI MySQL Connection Test"}

@app.get("/ESTADOS/")
def get_items(db: Session = Depends(get_db)):
    try:
        sql = "SELECT * FROM ESTADOS"
        # Executa a query usando a função genérica
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
