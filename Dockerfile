FROM amd64/python:3.7.12-slim-buster

ADD poetry.toml /
ADD poetry.lock /
ADD pyproject.toml /

RUN pip install poetry
RUN poetry install --no-root