# syntax=docker/dockerfile:1

FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 -y
RUN apt-get install cairosvg -y

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]