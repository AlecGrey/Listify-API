from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import InputRequired, Length, ValidationError
from datetime import datetime, date

class UserForm(FlaskForm):
    firstname = StringField('first name', validators=[InputRequired(), Length(min=1, max=30, message='Name must be less than 30 characters')])
    lastname = StringField('last name', validators=[InputRequired(), Length(min=1, max=30, message='Name must be less than 30 characters')])
    email = EmailField('email', validators=[InputRequired(), Length(min=7, max=50, message='Email must be less than 50 characters')])

class DepartmentForm(FlaskForm):
    name = StringField('department name', validators=[InputRequired(), Length(min=1, max=100, message='Dept name must be less than 100 characters')])

class ItemForm(FlaskForm):
    name = StringField('item name', validators=[InputRequired(), Length(min=1, max=100, message='Item name must be less than 100 characters')])
    department_id = SelectField('department', choices=[], validators=[InputRequired()])

class ListForm(FlaskForm):
    date = DateField('date', format='%Y-%m-%d', validators=[InputRequired()])
    user_id = SelectField('user', choices=[], validators=[InputRequired()])
    # custom validator
    def validate_date(self, field):
        print(field.data)
        if field.data < date.today():
            raise ValidationError('The date cannot be in the past!')

class RecipeForm(FlaskForm):
    name = StringField('recipe name', validators=[InputRequired(), Length(min=1, max=100, message='Recipe name must be less than 100 characters')])