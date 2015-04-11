from flask import Blueprint

fseasy = Blueprint('fseasy', __name__)

from . import views
