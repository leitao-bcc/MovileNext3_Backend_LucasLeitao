FROM python:3.6.8-jessie

RUN adduser flaskuser

WORKDIR /home/www

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY scheduled_delivery.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP scheduled_delivery.py

RUN chown -R flaskuser:flaskuser ./
USER flaskuser

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
