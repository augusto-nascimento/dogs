from typing import Optional, List

from fastapi import FastAPI, status

from schema import (
    Raca, Endereco, Cachorro, Saude
)
from model import create_tables
from controller import (
    raca_lista, raca_novo,
    cachorro_lista, cachorro_novo
)


app = FastAPI()


@app.get("/raca", response_model=List[Raca])
def get_raca():
    racas = raca_lista()
    return racas


@app.post("/raca", status_code=status.HTTP_201_CREATED)
def post_raca(raca: Raca):

    raca_novo(raca)

    return True


@app.get("/cachorro", response_model=List[Cachorro])
def get_cachorro():
    cachorros = cachorro_lista()
    return cachorros


@app.post("/cachorro", status_code=status.HTTP_201_CREATED)
def post_cachorro(cachorro: Cachorro):

    cachorro_novo(cachorro)

    return True


create_tables()