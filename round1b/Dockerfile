# Dockerfile (inside round1b/)

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY collections/ ./collections
COPY persona.json ./persona.json

ENTRYPOINT ["python", "-m", "src.main"]
