from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
# ~~ APP INITIALIZATION ~~ #
app = Flask(__name__)
app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))
# ~~ DB CONFIG ~~ #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
# ~~ INITIALIZE DATABASE ~~ #
db = SQLAlchemy(app)
# ~~ INITIALIZE MARSHMALLOW SERIALIZER ~~ #
ma = Marshmallow(app)

# ~~ IMPORT DATABASE SCHEMA ~~ #
from schema import User

# ~~ IMPORT ROUTES ~~ #
import routes
