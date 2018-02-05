from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) #  db migration for ease update
login = LoginManager(app) #  definition of login manager
login.login_view = 'login' #  login need an information of login view function's name

from app import routes, models