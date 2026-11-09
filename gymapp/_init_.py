from flask import Flask
from .extensions import db, appbuilder

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    db.init_app(app)
    appbuilder.init_app(app, db.session)
    
    return app