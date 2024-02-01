FROM python:3.10 as python-requirements-stage
WORKDIR /tmp
RUN pip install poetry
ENV PATH="$HOME/.poetry/bin:$PATH"
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --dev


# put it all together
FROM python:3.10 as run-stage
WORKDIR /code

## install dbmate
RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64
RUN chmod +x /usr/local/bin/dbmate

## install python deps
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y libpq5 postgresql-client # needed for psycopg3
COPY --from=python-requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --requirement /code/requirements.txt

COPY pyproject.toml /code
COPY setup-db.sh /code

## copy source
COPY ./app /code/app

## copy db migrations
COPY ./data/migrations /data/migrations

## start er up
EXPOSE 3339

CMD uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 3339
