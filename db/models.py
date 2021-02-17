from run import db

# ========================================
#                 USER
# ========================================

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

# ========================================
#                 LIST
# ========================================

class List(db.Model):
    # COLUMNS #
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        user = self.user
        return'<List - %s %s - %s>' % (user.firstname, user.lastname, self.date)