from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #init database
    db.init_app(app)

    #init bootstrap
    bootstrap.init_app(app)

    # attach routes and custom error pages here
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # attach routes to auth modules
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
