from pony.orm import db_session, select

from schema import (
    Raca as RacaSchema,
    Cachorro as CachorroSchema
)
from model import (
    Raca as RacaModel,
    Cachorro as CachorroModel,
    Endereco as EnderecoModel,
)

@db_session
def raca_lista():

    lista = []

    for raca in select(r for r in RacaModel).order_by(RacaModel.nome):
        lista.append(RacaSchema.from_orm(raca))

    return lista


@db_session
def raca_novo(raca_schema: RacaSchema):
    raca = RacaModel(**raca_schema.dict())


@db_session
def cachorro_lista():

    lista = []
    for cachorro in select(r for r in CachorroModel).order_by(CachorroModel.nome):
        lista.append(CachorroSchema.from_orm(cachorro))

    return lista


@db_session
def cachorro_novo(cachorro_schema: CachorroSchema):
    raca = RacaModel(**cachorro_schema.raca.dict())
    endereco = EnderecoModel(**cachorro_schema.endereco.dict())


    cachorro = CachorroModel(
        nome=cachorro_schema.nome,
        data_nascimento=cachorro_schema.data_nascimento,
        foto=cachorro_schema.foto,
        altura=cachorro_schema.altura,
        peso=cachorro_schema.peso,
        raca=raca,
        endereco=endereco,
        saude=cachorro_schema.saude
    )
