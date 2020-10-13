from datetime import date
from os import environ
from sys import modules
from decimal import Decimal

from pony.orm import (
    Required, Database, sql_debug, Optional, Set
)

if "pytest" in modules:
    database_name = 'test'
else:
    database_name = str(environ.get('SQL_DATABASE'))

db = Database()


class Raca(db.Entity):
    nome = Required(str)
    caracteristicas = Required(str)
    cachorro = Set('Cachorro')


class Endereco(db.Entity):
    estado = Required(str)
    municipio = Required(str)
    bairro = Required(str)
    cachorro = Optional("Cachorro")



class Cachorro(db.Entity):  # type: ignore
    nome = Required(str)
    data_nascimento = Optional(date)
    foto = Optional(str)
    altura = Required(Decimal)
    peso = Required(Decimal)
    raca = Required(Raca)
    endereco = Optional("Endereco")
    saude = Required(str)


sql_debug(True)
db.bind(
    provider='postgres',
    user=environ.get('SQL_USER'),
    password=environ.get('SQL_PWD'),
    host=environ.get('SQL_HOST'),
    database=database_name
)


def create_tables():
    db.generate_mapping(create_tables=True)
                                       