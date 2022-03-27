from flask import Blueprint

authentication = Blueprint('authentication', __name__, template_folder='../templates/auth')

from app.auth import routes
