from . import main
from flask import current_app, request

@main.route('/')
def index():
    current_app.logger.info('Main function index and from IP: %s', request.remote_addr)
    return '<h1>hello</h1>'
