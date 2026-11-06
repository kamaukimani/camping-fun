from flask import Flask 
from .config import Config
from .db import db,migrate
from .models import *
from .routes import *
from flask_cors import CORS

def create_app():
    
    app=Flask(__name__)
    app.config.from_object(Config)
    CORS(app,origins=["http://localhost:4000","http://127.0.0.1:4000"],supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(camper_bp,url_prefix="/campers")
    app.register_blueprint(activity_bp,url_prefix="/activities")
    app.register_blueprint(signup_bp,url_prefix="/signups")


    return app