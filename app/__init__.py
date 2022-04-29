from flask import Flask, render_template, Blueprint
import os
from requests import session
import config
from dotenv import load_dotenv
from flask_login import LoginManager

# ==================================== intern import  ==========================================
from app.models import db, migrate
from app.helpers.recursive import Recursive
from app.cmcAPI.api import Cmc 


# Global variables
login_manager = LoginManager()
api = Cmc()
def create_app():
    app = Flask(__name__)
    # =====================Inisialise the recusive of api call evry day (3624 seconds) ========
    rec = Recursive(3624,api.get_all())
    
    # ===========================Load environment variables from .env file=====================
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
    app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))

    # ========================Initialize the extentions (app factory===========================
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    # ======================================Database models ====================================
    from app.models.users import User
    from app.models.coins import Coin

    with app.app_context():
        db.create_all()
        db.session.commit()
        # =====================================Small HTTP Errors Handling========================
        @app.errorhandler(404)
        def page_not_found(e):
            return render_template('errors/404.html'), 40

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        # ============================================Blueprints=======================================
        # Blueprint for the non-auth parts of the app
        from app.views.home import home as home_blueprint
        app.register_blueprint(home_blueprint)
        # Blueprint for the auth parts of the app
        from app.views.auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)
        
        from app.views.coin import coins as coin_blueprint
        app.register_blueprint(coin_blueprint)
        app.config.get('SQLALCHEMY_DATABASE_URI').replace('%', '%%')
        return app
