from flask import Blueprint, render_template, redirect, url_for, request
from api import db
from api.database import models

admin = Blueprint("admin", __name__, template_folder='../templates')

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

@admin.route('/users/', methods=['GET'])
def users(errors=[]):
    # PRIMARY DATA:
    print(errors)
    return render_template('admin/show.html', table='user', data=None, rel_data=None)

@admin.route('/users/', methods=['POST'])
def create_user():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')

    errors = []

    try:
        db.session.add(models.User(
            firstname = firstname,
            lastname = lastname,
            email = email
        ))
        db.session.commit()
    except:
        errors.append('The user could not be created')

    return redirect(url_for('admin.users', errors = errors))

@admin.route('/departments/', methods=['GET'])
def departments():
    # PRIMARY DATA:
    return render_template('admin/show.html', table='department', data=None, rel_data=None)

@admin.route('/items/', methods=['GET'])
def items():
    # RELATIONAL DATA:
    def get_name(dept):
        return dept.name

    departments = models.Department.query.all()
    departments.sort(key=get_name)
    # PRIMARY DATA:
    return render_template('admin/show.html', table='item', data=None, rel_data=departments)

@admin.route('/lists/', methods=['GET'])
def lists():
    # RELATIONAL DATA:
    def get_lastname(user):
        return user.lastname
    
    users = models.User.query.all()
    users.sort(key=get_lastname)
    # PRIMARY DATA:
    return render_template('admin/show.html', table='list', data=None, rel_data=users)

@admin.route('/recipes/', methods=['GET'])
def recipes():
    #PRIMARY DATA:
    return render_template('admin/show.html', table='recipe', data=None, rel_data=None)