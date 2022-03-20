import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.tracker import *

db = SQLAlchemy()


def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    
    db.init_app(app)
    app.register_blueprint(main)

    return app

