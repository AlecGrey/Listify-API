from flask import jsonify, request
from run import app, db
from schema import User, user_schema, users_schema

# INDEX ROUTE
@app.route('/users/', methods=['GET'])
def user_index():
    users = User.query.all()

    return users_schema.jsonify(users)

# CREATE ROUTE
@app.route('/users/', methods=['POST'])
def user_create():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    email = request.json['email']

    new_user = User(firstname, lastname, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# SHOW ROUTE
@app.route('/users/<id>/', methods=['GET'])
def user_show(id):
    user = User.query.get(id)

    if user is None:
        return jsonify({
            "error": 404,
            "message": "No user was found with that ID"
        })
    else:
        return user_schema.jsonify(user)

# UPDATE ROUTE
@app.route('/users/<id>', methods=['PUT'])
def user_update(id):
    user = User.query.get(id)

    if user is None:
        return jsonify({
            "error": 404,
            "message": "No user was found with that ID"
        })
    
    User.query.filter_by(id=id).update(request.json)
    db.session.commit()

    return user_schema.jsonify(user)


