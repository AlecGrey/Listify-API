from flask import Blueprint, render_template
from api import db
from api.database import models

admin = Blueprint("admin", __name__, template_folder='../templates')

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

@admin.route('/users/', methods=['GET'])
def users():
    # PRIMARY DATA:
    return render_template('admin/show.html', table='user', data=None, rel_data=None)

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