from flask import Blueprint

blog = Blueprint('blog', __name__, url_prefix = '/', template_folder = 'templates')

from . import routes
