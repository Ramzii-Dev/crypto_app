from flask import Flask,render_template,Blueprint
import os
from requests import session
import config
from dotenv import load_dotenv 
from flask_login import LoginManager
from flask_migrate import Migrate 

import click 
from flask.cli import with_appcontext

app = Flask(__name__)
# ===========================Load environment variables from .env file=====================

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))


# Initialize the extentions (app factory
#======================================Database models ====================================
from app.models.users import User
from app.models import db




#=======================================migrations==========================================
migrate = Migrate(app,db)





#=====================================Small HTTP Errors Handling=============================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 40

login_manger = LoginManager()
login_manger.login_view = 'auth.login'
login_manger.init_app(app)

@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#============================================Blueprints=======================================
#Blueprint for the non-auth parts of the app
from app.views.home import home as home_blueprint
app.register_blueprint(home_blueprint)
#Blueprint for the auth parts of the app
from app.views.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


