import os
from flask import Flask
from flask_bootstrap import Bootstrap

from config import basedir, APPNAME

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

