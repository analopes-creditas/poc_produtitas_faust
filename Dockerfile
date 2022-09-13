FROM python:3.9-slim

RUN apt-get update

WORKDIR /core

COPY . /core

RUN pip install -r requirements.txt

RUN chmod 777 start_workers.sh

EXPOSE 8000
ENTRYPOINT ["./start_workers.sh"]
