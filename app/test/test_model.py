from datetime import date

import pytest
from pony.orm import db_session

from model import db, Raca, Endereco, Cachorro


class TestModel:
    def setup_method(self):
        try:
            db.generate_mapping(create_tables=True)
        except Exception:
            pass

        db.create_tables()

    def teardown_method(self):
        db.drop_all_tables(with_all_data=True)

    def test_novo_cachorro(self):
        with db_session:
            raca = Raca(
                nome="Shitzu",
                caracteristicas="fofinho"
            )

            endereco = Endereco(
                estado="SP",
                municipio = "Sao Paulo",
                bairro = "Barra Funda"
            )

            cachorro = Cachorro(
                nome="Floquinnho",
                data_nascimento=date(2019, 10, 1),
                foto="Base64",
                altura=0.30,
                peso=3.00,
                raca=raca,
                endereco=endereco,
                saude="ruim"
            )