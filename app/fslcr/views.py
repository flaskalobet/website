from flask import current_app, request
from . import fslcr

@fslcr.route('/fslcr/')
def index():
    current_app.logger.info('function fsindex and from IP: %s', request.remote_addr)
    return '<h1>FS LCR</h1>'

@fslcr.route('/fslcr/edit')
def edit():
    current_app.logger.info('function fsedit and from IP: %s', request.remote_addr)
    return '<h1>EDIT</h1>'

@fslcr.route('/fslcr/delete')
def delete():
    current_app.logger.info('function fsdelete and from IP: %s', request.remote_addr)
    return '<h1>DELETE</h1>'

