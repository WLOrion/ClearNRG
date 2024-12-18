# inserir_estados.py

from sqlalchemy.orm import Session
from ..database import engine
from ..models import Estado

def inserir_estados():
    estados = [
        {'id': 12, 'nome': 'Acre', 'sigla': 'AC'},
        {'id': 27, 'nome': 'Alagoas', 'sigla': 'AL'},
        {'id': 13, 'nome': 'Amazonas', 'sigla': 'AM'},
        {'id': 16, 'nome': 'Amapá', 'sigla': 'AP'},
        {'id': 29, 'nome': 'Bahia', 'sigla': 'BA'},
        {'id': 23, 'nome': 'Ceará', 'sigla': 'CE'},
        {'id': 53, 'nome': 'Distrito Federal', 'sigla': 'DF'},
        {'id': 32, 'nome': 'Espírito Santo', 'sigla': 'ES'},
        {'id': 52, 'nome': 'Goiás', 'sigla': 'GO'},
        {'id': 21, 'nome': 'Maranhão', 'sigla': 'MA'},
        {'id': 31, 'nome': 'Minas Gerais', 'sigla': 'MG'},
        {'id': 50, 'nome': 'Mato Grosso do Sul', 'sigla': 'MS'},
        {'id': 51, 'nome': 'Mato Grosso', 'sigla': 'MT'},
        {'id': 15, 'nome': 'Pará', 'sigla': 'PA'},
        {'id': 25, 'nome': 'Paraíba', 'sigla': 'PB'},
        {'id': 26, 'nome': 'Pernambuco', 'sigla': 'PE'},
        {'id': 22, 'nome': 'Piauí', 'sigla': 'PI'},
        {'id': 41, 'nome': 'Paraná', 'sigla': 'PR'},
        {'id': 33, 'nome': 'Rio de Janeiro', 'sigla': 'RJ'},
        {'id': 24, 'nome': 'Rio Grande do Norte', 'sigla': 'RN'},
        {'id': 43, 'nome': 'Rio Grande do Sul', 'sigla': 'RS'},
        {'id': 11, 'nome': 'Rondônia', 'sigla': 'RO'},
        {'id': 14, 'nome': 'Roraima', 'sigla': 'RR'},
        {'id': 42, 'nome': 'Santa Catarina', 'sigla': 'SC'},
        {'id': 35, 'nome': 'São Paulo', 'sigla': 'SP'},
        {'id': 28, 'nome': 'Sergipe', 'sigla': 'SE'},
        {'id': 17, 'nome': 'Tocantins', 'sigla': 'TO'}
    ]

    with Session(engine) as session:
        # Verifica se os estados já foram inseridos
        if session.query(Estado).first():
            print("Estados já inseridos.")
            return

        for estado_data in estados:
            estado = Estado(**estado_data)
            session.add(estado)
        session.commit()
        print("Estados inseridos com sucesso.")

if __name__ == "__main__":
    inserir_estados()
