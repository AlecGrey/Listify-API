from run import db, ma

# ======================================================
#                        - MODEL -
# ======================================================

class List(db.Model):
    # COLUMNS #
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        user = self.user
        return'<List - %s %s - %s>' % (user.firstname, user.lastname, self.date)

# ======================================================
#                       - SCHEMA -
# ======================================================

class ListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date')

# Initialize User Schema
user_schema = ListSchema()
users_schema = ListSchema(many=True)