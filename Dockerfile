FROM python:3.6-alpine
MAINTAINER Alistair Webster "alistairkwebster@gmail.com"

RUN mkdir -p   /crawler
COPY app /crawler/app
COPY crawler /crawler/crawler
COPY crawler_outputs /crawler/crawler_outputs
COPY main.py /crawler/main.py
COPY config.py /crawler/config.py
COPY constants.py /crawler/constants.py
COPY scrapy.cfg /crawler/scrapy.cfg
COPY requirements.txt /crawler/requirements.txt


WORKDIR /crawler
RUN apk add --no-cache --virtual .pynacl_deps ca-certificates openssl-dev gcc libxml2-dev libxslt-dev libc-dev unixodbc-dev build-base python3-dev libffi-dev
RUN apk add --update py-pip

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "main.py"]