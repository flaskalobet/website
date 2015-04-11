from flask import Blueprint

fsuser = Blueprint('fsuser', __name__)

from . import views
