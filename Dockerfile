FROM python:3.7-alpine

ENV FLASK_APP webUI
ENV FLASK_CONFIG production

RUN adduser -D flask
WORKDIR /home/flask

COPY . ./
RUN rm -rf instance 2> /dev/null
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN chmod +x boot.sh

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
