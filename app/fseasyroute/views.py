from flask import current_app, request
from . import fseasy

@fseasy.route('/fseasy/')
def index():
    current_app.logger.info('function fsindex and from IP: %s', request.remote_addr)
    return '<h1>FS USER</h1>'

@fseasy.route('/fseasy/edit')
def edit():
    current_app.logger.info('function fsedit and from IP: %s', request.remote_addr)
    return '<h1>EDIT</h1>'

@fseasy.route('/fseasy/delete')
def delete():
    current_app.logger.info('function fsdelete and from IP: %s', request.remote_addr)
    return '<h1>DELETE</h1>'

