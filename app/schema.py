from typing import List, Optional
from datetime import date
from enum import Enum

from pydantic import BaseModel


class Raca(BaseModel):
    nome: str
    caracteristicas: str

    class Config:
        orm_mode = True


class Endereco(BaseModel):
    estado: str
    municipio: str
    bairro: str

    class Config:
        orm_mode = True

class Saude(str, Enum):
    ruim = 'ruim'
    cuidado = 'precisa cuidado'
    bom = 'bom'

    class Config:
        orm_mode = True

class Cachorro(BaseModel):
    nome: str
    data_nascimento: date
    foto: str
    altura: float
    peso: float
    raca: Raca
    endereco: Endereco
    saude : Saude

    class Config:
        orm_mode = True