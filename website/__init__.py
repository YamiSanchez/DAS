from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    app.app_context().push()
    db.create_all()

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import User, Post, Comment, Like

    return app


