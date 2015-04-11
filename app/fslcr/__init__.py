from flask import Blueprint

fslcr = Blueprint('fslcr', __name__)

from . import views
