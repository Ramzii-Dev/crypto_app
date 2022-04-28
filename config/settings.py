import os

from flask import current_app 
class Config:
    DEFAULT = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = os.environ.get('APP_NAME')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    current_app.config.get('SQLALCHEMY_DATABASE_URI').replace('%', '%%')
class development(Config):
    DEBUG = True
    

class production(Config):
    DEBUG = False
    PORT = os.environ.get('PORT') or 8080