FROM python:3.6.4-alpine

COPY requirements* /temp/

RUN pip install -r /temp/requirements.txt -r /temp/requirements_dev.txt

COPY . /algorithm_services

WORKDIR /algorithm_services

EXPOSE 5000

CMD python server.py
