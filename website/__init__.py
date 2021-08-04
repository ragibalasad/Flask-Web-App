from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    # Initialize app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '$rbn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Register external routes as blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Render custom Error404
    @app.errorhandler(404)
    def error404(error):
        return render_template('404.html'), 404

    # Initialize Database
    from .models import User, Post
    create_database(app)

    # Initialize login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# Creates database.db file in path if doesn't exist
def create_database(app):
    if not path.exists('database/' + DB_NAME):
        db.create_all(app=app)
        print('Database Doesn\'t exist. New database created!')