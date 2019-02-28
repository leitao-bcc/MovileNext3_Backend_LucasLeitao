FROM python:3.6-alpine

RUN adduser -D flaskuser

WORKDIR /home/www

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY ifood_api.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP ifood_api.py

RUN chown -R flaskuser:flaskuser ./
USER flaskuser

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]