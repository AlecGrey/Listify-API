from flask import Blueprint, render_template, jsonify, request
from run import db
from schema import User, user_schema, users_schema

users = Blueprint("users", __name__)

# INDEX ROUTE
@users.route('/', methods=['GET'])
def index():
    users = User.query.all()

    return users_schema.jsonify(users)

# CREATE ROUTE
@users.route('/', methods=['POST'])
def create():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']
    
    new_user = User(firstname, lastname, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# SHOW ROUTE
@users.route('/<id>/', methods=['GET'])
def show(id):
    user = User.query.get(id)

    if user is None:
        return jsonify({
            "error": 404,
            "message": "No user was found with that ID"
        })
    else:
        return user_schema.jsonify(user)

# UPDATE ROUTE
@users.route('/<id>', methods=['PUT'])
def update(id):
    user = User.query.get(id)

    if user is None:
        return jsonify({
            "error": 404,
            "message": "No user was found with that ID"
        })
    
    User.query.filter_by(id=id).update(request.json)
    db.session.commit()

    return user_schema.jsonify(user)
