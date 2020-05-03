FROM python:3.8

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY poetry.lock .
COPY pyproject.toml .

ARG env=prod
RUN pip install poetry==1.0.2 --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry install `if test $env = prod || test $env = dev ; then echo "--no-dev" ; fi` && \
    rm -rf /root/.cache/pypoetry

COPY . .

ENV ENV=$env
CMD alembic upgrade head && \
    uvicorn --host=0.0.0.0 app.main:app `if test $ENV = dev ; then echo "--reload" ; fi`
