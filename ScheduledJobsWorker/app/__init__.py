from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from app import routes

scheduler = BackgroundScheduler({'apscheduler.timezone': 'America/Sao_Paulo'})


def create_app():
    app = Flask(__name__)

    scheduler.start()

    return app
