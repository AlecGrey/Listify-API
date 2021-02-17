from run import db, ma

#=============================
#       --- USERS ---
#=============================

# User Model
class User(db.Model):
    # COLUMNS #
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return'<User %s %s, email: %s>' % (self.firstname, self.lastname, self.email)

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email')

# Initialize User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)