# 1. Base image: a minimal Linux + Python 3.11 runtime on AMD64
FROM --platform=linux/amd64 python:3.13.5-slim

# 2. Set working directory inside the container to /app
WORKDIR /app

# 3. Copy your requirements.txt into /app and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your code
COPY batch_run.py .
COPY src/ ./src

# 5. Ensure the outputs directory exists inside the container
RUN mkdir outputs

# 6. When someone runs the container, execute this command by default
ENTRYPOINT ["python", "batch_run.py"]
CMD []
