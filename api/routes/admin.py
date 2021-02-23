from flask import Blueprint, render_template, redirect, url_for, request, flash
from api import db
from api.database import models
from api.forms import UserForm, DepartmentForm, ItemForm, ListForm, RecipeForm
from datetime import datetime

admin = Blueprint("admin", __name__, template_folder='../templates')

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

# =================================================
#                   USER ROUTES
# =================================================

def get_all_users():
    return models.User.query.all()

@admin.route('/users/', methods=['GET'])
def users():
    return render_template('admin/show.html', table='user', form=UserForm(), data=get_all_users())

@admin.route('/users/', methods=['POST'])
def create_user():
    form = UserForm()
    # IF FRONTEND VALIDATION FAILS
    if not form.validate_on_submit():
        return render_template('admin/show.html', table='user', form=form, data=get_all_users())
    # ATTEMPT TO SAVE USER
    try:
        db.session.add(models.User(
            firstname = request.form.get('firstname'),
            lastname = request.form.get('lastname'),
            email = request.form.get('email')
        ))
        db.session.commit()
    except:
        db.session.rollback()
        flash('The user could not be created in the database.', 'error-flash')
        return render_template('admin/show.html', table='user', form=form, data=get_all_users())
    # IF THE USER SUCCESSFULLY SAVED
    flash('User created successfully!', 'success-flash')
    return redirect(url_for('admin.users'))

# =================================================
#                DEPARTMENT ROUTES
# =================================================

def get_all_departments():
    return models.Department.query.all()

@admin.route('/departments/', methods=['GET'])
def departments():
    # PRIMARY DATA:
    return render_template('admin/show.html', table='department', form=DepartmentForm(), data=get_all_departments())

@admin.route('/departments/', methods=['POST'])
def create_department():
    form = DepartmentForm()
    # FRONTEND VALIDATION FAILS
    if not form.validate_on_submit():
        return render_template('admin/show.html', table='department', form=form, data=get_all_departments())
    # ATTEMPT TO SAVE USER
    try:
        db.session.add(models.Department(
            name = request.form.get('name')
        ))
        db.session.commit()
    except:
        db.session.rollback()
        flash('the department could not be created in the database', 'error-flash')
        return render_template('admin/show.html', table='department', form=form, data=get_all_departments())
    # IF SAVE WAS SUCCESSFUL
    flash('Department created successfully!', 'success-flash')
    return redirect(url_for('admin.departments'))

# =================================================
#                   ITEM ROUTES
# =================================================

def construct_item_form():
    form = ItemForm()
    choices = [(None, 'Select one')]
    for dept in models.Department.query.order_by('name'):
        choices.append(( dept.id, dept.name ))
    form.department_id.choices = choices
    return form

@admin.route('/items/', methods=['GET'])
def items():
    # PRIMARY DATA:
    return render_template('admin/show.html', table='item', form=construct_item_form())

@admin.route('/items/', methods=['POST'])
def create_item():
    # WTFORM
    form = construct_item_form()
    # form fails validations, return to template with errors
    if not form.validate_on_submit():
        return render_template('admin/show.html', table='item', form=form)

    errors = []
    # SAVE USER
    try:
        department = models.Department.query.filter_by(id=request.form.get('department_id')).first()
        db.session.add(models.Item(
            name = request.form.get('name'),
            department = department
        ))
        db.session.commit()
    except:
        errors.append('The item could not be created')
    # was db submission successful?
    success = len(errors) == 0
    # render template with errors & success bool:
    return render_template('admin/show.html', table='item', form=form, errors=errors, success=success)

# =================================================
#                   LIST ROUTES
# =================================================

def construct_list_form():
    form = ListForm()
    choices = [(None, 'Select one')]
    for user in models.User.query.order_by('lastname'):
        choices.append(( user.id, f"{user.lastname}, {user.firstname} - {user.email}" ))
    form.user_id.choices = choices
    return form

@admin.route('/lists/', methods=['GET'])
def lists():
    # PRIMARY DATA:
    return render_template('admin/show.html', table='list', form=construct_list_form())

@admin.route('/lists/', methods=['POST'])
def create_list():
    #WTFORM
    form = construct_list_form()
    # form fails validations, return to template with errors
    if not form.validate_on_submit():
        return render_template('admin/show.html', table='list', form=form)

    errors = []
    # SAVE USER
    try:
        user = models.User.query.filter_by(id=request.form.get('user_id')).first()
        db.session.add(models.List(
            date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
            user = user
        ))
        db.session.commit()
    except:
        errors.append('The list could not be created')
    # was db submission successful?
    success = len(errors) == 0
    # render template with errors & success bool:
    return render_template('admin/show.html', table='list', form=form, errors=errors, success=success)
    
# =================================================
#                   RECIPE ROUTES
# =================================================

@admin.route('/recipes/', methods=['GET'])
def recipes():
    #PRIMARY DATA:
    return render_template('admin/show.html', table='recipe', form=RecipeForm())

@admin.route('/recipes/', methods=['POST'])
def create_recipe():
    form = RecipeForm()
    # form fails validations, return to template with errors
    if not form.validate_on_submit():
        return render_template('admin/show.html', table='recipe', form=form)

    errors = []
    # SAVE USER
    try:
        db.session.add(models.Recipe(
            name = request.form.get('name')
        ))
        db.session.commit()
    except:
        errors.append('The recipe could not be created')
    # was db submission successful?
    success = len(errors) == 0
    # render template with errors & success bool:
    return render_template('admin/show.html', table='recipe', form=form, errors=errors, success=success)


