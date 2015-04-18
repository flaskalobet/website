from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from config import config

from logging import Formatter, INFO, WARNING, DEBUG, getLogger
from logging.handlers import RotatingFileHandler

bootstrap = Bootstrap()
db = SQLAlchemy()

#: logger modules
filehandler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)

#: Set Formatter of log modules
formatter = Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} - %(message)s")
filehandler.setFormatter(formatter)

#: set Level of log - INFO, WARNING, DEBUG
#: the flask app should be the same setLevel of log of logging modules
filehandler.setLevel(INFO)


#: Flask-login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #: set Level of log - INFO, WARNING, DEBUG
    #: the flask app should be the same setLevel of log of logging modules
    app.logger.setLevel(INFO)

    #: Begging log app
    app.logger.addHandler(filehandler)

    #: import blueprint
    from main import main
    app.register_blueprint(main)

    #: import blueprint fsuser
    from fsuser import fsuser
    app.register_blueprint(fsuser)

    #: import blueprint fseasyrouting
    from fseasyroute import fseasy
    app.register_blueprint(fseasy)

    #: import blueprint fslcr
    from fslcr import fslcr
    app.register_blueprint(fslcr)

    return app
