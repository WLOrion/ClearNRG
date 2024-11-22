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
    
@app.get("/ventos/velocidade_maxima_por_cidade/")
def get_velocidade_maxima_por_cidade(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT c.nome AS cidade, MAX(d.velocidade_maxima) AS velocidade_maxima_registrada
        FROM DADOS_EOLICOS d
        JOIN CIDADES c ON d.cidade_id = c.id
        GROUP BY cidade;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ventos/rajada_maxima_por_cidade/")
def get_rajada_maxima_por_cidade(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT c.nome AS cidade, MAX(d.rajada_maxima) AS rajada_maxima_registrada
        FROM DADOS_EOLICOS d
        JOIN CIDADES c ON d.cidade_id = c.id
        GROUP BY cidade;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/solares/tendencia_anual_cidade/")
def get_tendencia_anual_cidade(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT c.nome AS cidade, MONTH(d.tempo) AS mes, YEAR(d.tempo) AS ano, SUM(d.incidencia_solar) AS incidencia_anual
        FROM DADOS_SOLARES d
        JOIN CIDADES c ON d.cidade_id = c.id
        GROUP BY cidade, mes, ano
        ORDER BY cidade, mes, ano;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/solares/tendencia_anual_estado/")
def get_tendencia_anual_estado(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT e.nome AS estado, MONTH(d.tempo) AS mes, YEAR(d.tempo) AS ano, SUM(d.incidencia_solar) AS incidencia_anual
        FROM DADOS_SOLARES d
        JOIN CIDADES c ON d.cidade_id = c.id
        JOIN ESTADOS e ON c.estado_id = e.id 
        GROUP BY estado, mes, ano
        ORDER BY estado, mes, ano;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ventos/media_rajada_por_cidade/")
def get_media_rajada_por_cidade(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT c.nome AS cidade, DATE(d.tempo) AS data, AVG(d.rajada_maxima) AS media_rajada_maxima
        FROM DADOS_EOLICOS d
        JOIN CIDADES c ON d.cidade_id = c.id
        GROUP BY cidade, data
        ORDER BY cidade, data;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ventos/media_duracao_vento_por_cidade/")
def get_media_duracao_vento_por_cidade(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT c.nome AS cidade, AVG(CAST(d.duracao AS DECIMAL)) AS media_duracao_vento
        FROM DADOS_EOLICOS d
        JOIN CIDADES c ON d.cidade_id = c.id
        GROUP BY cidade
        ORDER BY cidade;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ventos/media_rajada_por_estado/")
def get_media_rajada_por_estado(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT e.nome AS estado, DATE(d.tempo) AS data, AVG(d.rajada_maxima) AS media_rajada_maxima
        FROM DADOS_EOLICOS d
        JOIN CIDADES c ON d.cidade_id = c.id
        JOIN ESTADOS e ON c.estado_id = e.id
        GROUP BY estado, data
        ORDER BY estado, data;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ventos/tendencia_anual_rajada/")
def get_tendencia_anual_rajada(db: Session = Depends(get_db)):
    try:
        sql = """
        SELECT YEAR(d.tempo) AS ano, MONTH(d.tempo) AS mes, AVG(d.rajada_maxima) AS media_rajada_maxima
        FROM DADOS_EOLICOS d
        GROUP BY ano, mes
        ORDER BY ano, mes;
        """
        results = execute_query(db, sql)
        return {"results": [row._asdict() for row in results]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
