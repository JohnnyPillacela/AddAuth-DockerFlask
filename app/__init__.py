"""Initialize app."""
from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from flask_session import Session


patch_all()
db = SQLAlchemy()
login_manager = LoginManager()
mysql = MySQL(cursorclass=DictCursor)
sess = Session()


def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
    app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'citiesData'
    mysql.init_app(app)
    sess.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import
        import routes
        import auth
        from assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        #db.create_all()

        #if app.config['FLASK_ENV'] == 'development':
         #   compile_static_assets(app)

        return app
