from flask import Blueprint

home = Blueprint("home", __name__)

@home.route('/', methods=['GET'])
def root():
    return "<h1>Listify API</h1>"
    # RENDER A VIEW!