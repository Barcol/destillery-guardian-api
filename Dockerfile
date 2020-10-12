FROM python:3.7

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 80

COPY ./alembic ./alembic
COPY ./alembic.ini ./alembic.ini
COPY ./script.sh ./script.sh

CMD ["./script.sh"]
