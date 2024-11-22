from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, BIGINT
from sqlalchemy.orm import relationship

Base = declarative_base()

class Estado(Base):
    __tablename__ = 'ESTADOS'

    id = Column(TINYINT(unsigned=True), primary_key=True, autoincrement=False)
    nome = Column(String(20), nullable=False)
    sigla = Column(String(2), nullable=False)

    cidades = relationship('Cidade', back_populates='estado', cascade="all, delete")

class Cidade(Base):
    __tablename__ = 'CIDADES'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    estado_id = Column(TINYINT(unsigned=True), ForeignKey('ESTADOS.id', ondelete='CASCADE'), nullable=False)
    latitude = Column(DECIMAL(8, 5), nullable=False)
    longitude = Column(DECIMAL(8, 5), nullable=False)

    estado = relationship('Estado', back_populates='cidades')
    dados_eolicos = relationship('DadosEolicos', back_populates='cidade', cascade="all, delete")
    dados_solares = relationship('DadosSolares', back_populates='cidade', cascade="all, delete")

class DadosEolicos(Base):
    __tablename__ = 'DADOS_EOLICOS'

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    cidade_id = Column(INTEGER(unsigned=True), ForeignKey('CIDADES.id', ondelete='CASCADE'), nullable=False)
    tempo = Column(TIMESTAMP, nullable=False)
    duracao = Column(String(10), nullable=False)
    rajada_maxima = Column(DECIMAL(5, 2), nullable=False)
    velocidade_maxima = Column(DECIMAL(5, 2), nullable=False)

    cidade = relationship('Cidade', back_populates='dados_eolicos')

class DadosSolares(Base):
    __tablename__ = 'DADOS_SOLARES'

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    cidade_id = Column(INTEGER(unsigned=True), ForeignKey('CIDADES.id', ondelete='CASCADE'), nullable=False)
    tempo = Column(TIMESTAMP, nullable=False)
    radiacao_anual = Column(BIGINT(unsigned=True), nullable=False)
    incidencia_solar = Column(BIGINT(unsigned=True), nullable=False)

    cidade = relationship('Cidade', back_populates='dados_solares')
