from flask import Flask

def create_app():

    app = Flask(__name__)

    app.secret_key = '123'

    with app.app_context():

        from . import rotas

    return app