FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY uv.lock pyproject.toml /app/
RUN apt update && \
    uv sync --frozen --no-cache --no-dev

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT []

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload
