from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# ~~ APP INITIALIZATION ~~ #
app = Flask(__name__)

# ~~ DB CONFIG ~~ #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listify_api_development.sqlite3'

# ~~ INITIALIZE DATABASE & SERIALIZER ~~ #
db = SQLAlchemy(app)
ma = Marshmallow(app)

# ROUTES
from api.routes import home, users, admin

# ~~ MAP ROUTES AS BLUEPRINTS ~~ #
app.register_blueprint(home, url_prefix='')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(admin, url_prefix='/admin')