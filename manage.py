#from flask import Flask, request
from config import config
from logging import Formatter, INFO, WARNING, DEBUG, getLogger
from logging.handlers import RotatingFileHandler

from app import create_app, db

app = create_app('default')

#app = Flask(__name__)
#app.config.from_object(config['default'])


#@app.errorhandler(404)
#def page_not_found(e):
#    app.logger.info('Info Page Not Found: %s', request)
#    return '404'


#@app.route('/')
#def index():
#    app.logger.info('Info: %s', request)
#    return 'hello'


if __name__ == '__main__':
    app.run(host=config['server'])
