FROM ubuntu:focal

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && pip3 install -U pip setuptools \
    && pip3 install pipenv

WORKDIR /usr/src/app
COPY ["Pipfile", "Pipfile.lock", "/usr/src/app/"]
RUN pipenv install
COPY . /usr/src/app/
# ENTRYPOINT pipenv run uvicorn app:app --host 0.0.0.0 --port 8000 --reload