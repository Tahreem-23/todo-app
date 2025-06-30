from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
    app.config['SECRET_KEY']='NEWEST'
    app.config['track_modifications']=False
    db.__init__(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app