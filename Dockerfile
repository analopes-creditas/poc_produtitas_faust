FROM python:3.9.13

WORKDIR /core

COPY . /core

RUN pip install -r requirements.txt

ENTRYPOINT ["./run.sh"]
