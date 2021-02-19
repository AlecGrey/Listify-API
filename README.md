# Introduction
This is the directory for the Python Flask API for Listify.

## Technologies added to this Flask Application

- SQLAlchemy - ORM tool for defining SQL tables, including relational database tables
- Flask-Migrate - Handles DB migrations for safe version control and DB changes without losing data
- Jinja - static pages with nested components, includes Python logic
- WTForms (TBD) - Library to assist in form creation and validation handling

## To-do List

* [X] ~~*Finish validations for all current models*~~ [2021-02-19]
* [ ] Create Admin pages to allow user to input data, delete records
    * [ ] Create separate page for each non-join model, includes:
        * Form to create new instance of model, with validations
        * Table to browse all instances, with delete buttons
    * [ ] Create show page for User, recipe, and list that allows addition of has-many-through connections
        * Recipe can add Item instances via Ingredient joiner
        * List can add Recipe instances via ListRecipe joiner
        * List can add Item instances via ListItem joiner
        * User can add Recipe instances via FavoriteRecipe joiner
