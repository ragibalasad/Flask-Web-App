from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from os import getenv

load_dotenv(override=True)
DB_URI = getenv("DB_URI")
SECRET_KEY = getenv("SECRET_KEY")
db = SQLAlchemy()


def create_app():
    # Initialize app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    db.init_app(app)

    # Register external routes as blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Render custom Error404
    @app.errorhandler(404)
    def error404(error):
        return render_template("404.html"), 404

    # Initialize Database
    from .models import User, Post

    # Create database if does not exist already
    with app.app_context():
        db.create_all()

    # Initialize login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
