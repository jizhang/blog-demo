FROM python:3.11-slim

ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install poetry==1.7.1 && \
    $POETRY_HOME/bin/poetry config virtualenvs.create false

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN $POETRY_HOME/bin/poetry install --without dev --extras gunicorn

COPY poetrydemo/ ./poetrydemo/
