FROM python:3.9-slim-buster

ENV PORT 8080
ENV HOST 0.0.0.0
ENV PYTHONUNBUFFERED True

COPY . /app
WORKDIR /app

RUN apt-get update \
    && apt-get install -qq -y build-essential libssl-dev libffi-dev python3-pip git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN --mount=type=ssh pip3 install -r requirements.txt && pip3 install --no-cache-dir gunicorn==20.1.0 uvicorn[standard]

EXPOSE 8080

CMD exec gunicorn -b :$PORT --workers 6 --timeout 0 -k uvicorn.workers.UvicornWorker --reload main:general_pages_router