from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, execute_query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI MySQL Connection Test"}

@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    try:
        sql = "<coloque a query aqui>"
        # Executa a query usando a função genérica
        results = execute_query(db, sql)
        return {"results": [dict(row) for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
