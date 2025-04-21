FROM python:3.12-slim

WORKDIR /src

COPY pyproject.toml ./
RUN pip install poetry==1.8.3 && poetry config virtualenvs.create false && poetry install

COPY . .
