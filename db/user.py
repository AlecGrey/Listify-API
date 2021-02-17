from run import db, ma
from db.list import ListSchema

# ======================================================
#                        - MODEL -
# ======================================================

class User(db.Model):
    # COLUMNS #
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    lists = db.relationship('List', backref='user')

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return'<User - %s %s - %s>' % (self.firstname, self.lastname, self.email)

# ======================================================
#                       - SCHEMA -
# ======================================================

class UserSchema(ma.Schema):
    lists = ma.Nested(ListSchema, many=True)

    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email', 'lists')

# Initialize User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)