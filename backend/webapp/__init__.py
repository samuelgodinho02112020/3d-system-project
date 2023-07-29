from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_jwt_extended import JWTManager

app = Flask(__name__)

import config as config

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app,db)
CORS(app)

from webapp.models.users import Users

import webapp.views.users

