FROM python:3.10-slim

RUN apt-get clean && apt-get update
RUN pip install --upgrade pip

RUN apt-get install -y python3 python3-pip python3-venv

RUN apt update

RUN apt-get update
RUN apt-get install -y python3-dev libpq-dev
RUN export PATH=$PATH:/path/to/pg_config
RUN pip install psycopg2-binary
RUN pip install psycopg2

RUN apt-get install libpq-dev

WORKDIR /app/

RUN apt update

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ResumeBackEnd/main.py

CMD python3 ResumeBackEnd/main.py
