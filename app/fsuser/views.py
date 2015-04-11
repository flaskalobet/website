from flask import current_app, request
from . import fsuser

@fsuser.route('/fsuser/')
def index():
    current_app.logger.info('function fsindex and from IP: %s', request.remote_addr)
    return '<h1>FS USER</h1>'

@fsuser.route('/fsuser/get')
def get():
    current_app.logger.info('function fsget and from IP: %s', request.remote_addr)
    return '<h1>GET FS USER</h1>'

@fsuser.route('/fsuser/edit')
def edit():
    current_app.logger.info('function fsedit and from IP: %s', request.remote_addr)
    return '<h1>EDIT</h1>'

@fsuser.route('/fsuser/delete')
def delete():
    current_app.logger.info('function fsdelete and from IP: %s', request.remote_addr)
    return '<h1>DELETE</h1>'

