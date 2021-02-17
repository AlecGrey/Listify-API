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

# ~~ INITIALIZE DATABASE & SERIALIZER ~~ #
db = SQLAlchemy(app)
ma = Marshmallow(app)

# ROUTES
import routes

# ~~ ROUTING BLUEPRINTS ~~ #
app.register_blueprint(routes.home, url_prefix='')
app.register_blueprint(routes.users, url_prefix='/users')