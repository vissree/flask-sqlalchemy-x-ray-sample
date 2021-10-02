from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.ext.flask_sqlalchemy.query import XRayFlaskSqlAlchemy


app = Flask(__name__, instance_relative_config=False)
xray_recorder.configure(service="Flask-SQLAlchemy-X-Ray-Sample")
XRayMiddleware(app, xray_recorder)
app.config.from_object("config.Config")

db = XRayFlaskSqlAlchemy(app)


def create_app():
    with app.app_context():
        from . import routes

        db.create_all()

        return app
