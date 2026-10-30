# syntax=docker/dockerfile:1


FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /app/venv
COPY fake_app.py .

WORKDIR /data

ENTRYPOINT ["python", "/app/fake_app.py"]
