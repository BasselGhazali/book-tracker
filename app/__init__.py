import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
styling = Bootstrap()


def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    styling.init_app(app)
    
    app.register_blueprint(main)
    app.register_blueprint(authentication)

    return app


from app.tracker import *
from app.auth import authentication
