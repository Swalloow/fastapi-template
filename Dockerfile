FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir -p /app/app
COPY ./app /app/app
COPY ./requirements.txt /app/app/requirements.txt

RUN pip install -r /app/app/requirements.txt
