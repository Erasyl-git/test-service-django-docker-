FROM python:3.11.6
COPY requirements.txt /temp/

COPY service /service
WORKDIR /service
EXPOSE 8000
RUN pip intall -r /temp/requirements.txt

RUN adduser --disabled-password service-user


USER service-user

