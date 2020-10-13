#!/bin/bash

sleep 10

export PYTHONPATH=`pwd`
export SQLALCHEMY_DATABASE_URL=postgres://user:pass@database:5432/my-db-name

alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 80
