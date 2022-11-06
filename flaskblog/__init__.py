import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = '11f1872262914950dcc982641b87f24d3a5fb163bb5bcaae61c4223f25ce8f3e'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)

    return app


app = create_app()
app.app_context().push()
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)