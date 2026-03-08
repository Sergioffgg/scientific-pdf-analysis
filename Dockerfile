FROM python:3.13

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

COPY src /app/src

COPY input /app/input
COPY output /app/output

CMD ["python", "src/trabajo1/main.py"]
