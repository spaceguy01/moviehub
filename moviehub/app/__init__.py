# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask.ext.bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type +'.py')
    #'/Users/Ergosphere/Desktop/ProgrammingFiles/Flask/moviehub/config/dev.py'
    app.config.from_pyfile(configuration)

    db.init_app(app) # bind database to flask
    bootstrap.init_app(app) # initialize bootstrap
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.moviehub import main  # import blueprint
    app.register_blueprint(main) # register blueprint

    from app.auth import authentication  # import authentication
    app.register_blueprint(authentication)  # register blueprint

    return app
