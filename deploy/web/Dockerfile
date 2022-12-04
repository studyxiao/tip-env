# build stage
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential gcc musl-dev && \
    rm -rf /var/lib/apt/lists/*

# install PDM
RUN pip install -U pip setuptools wheel pdm 

# install dependence
COPY pyproject.toml pdm.lock /app/
RUN mkdir __pypackages__ && pdm install --prod --no-lock --no-editable

# run stage
FROM python:3.11-slim-bullseye

ENV TZ=Asia/Shanghai

WORKDIR /app

ENV PYTHONPATH=/app/pkgs
COPY --from=builder /app/__pypackages__/3.11/lib /app/pkgs
COPY . .

CMD ["python", "-m", "gunicorn", "--worker-tmp-dir", "/dev/shm", "--config", "python:config.gunicorn", "app:app"]
