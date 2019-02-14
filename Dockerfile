FROM python:3.7-alpine

ENV FLASK_APP webUI
ENV FLASK_CONFIG production

RUN adduser -D flask
WORKDIR /home/flask

RUN apk update && apk add iputils

COPY . ./
RUN rm -rf instance 2> /dev/null
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN chmod +x boot.sh
RUN chmod +x worker.py

RUN chown -R flask:flask ./
USER flask

Run mkdir instance/
RUN mv web-application.cfg instance/

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
