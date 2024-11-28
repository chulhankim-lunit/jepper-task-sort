FROM python:3.11-bullseye

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-root --no-dev

COPY . .

ENTRYPOINT ["python", "-m", "app.main"]
