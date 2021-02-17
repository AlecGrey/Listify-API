from run import db

# ========================================
#                 USER
# ========================================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    # has_many
    lists = db.relationship('List', backref='user')

    def __repr__(self):
        return'<User - %s %s - %s>' % (self.firstname, self.lastname, self.email)

# ========================================
#                 LIST
# ========================================

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    # belongs_to
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # has_many
    list_items = db.relationship('ListItem', backref='list')

    @property
    def items(self):
        items = ListItem.query.filter_by(list_id = self.id)
        return items.all()

    def __repr__(self):
        user = self.user
        return'<List - %s %s - %s>' % (user.firstname, user.lastname, self.date)

# ========================================
#               DEPARTMENT
# ========================================

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # has_many
    items = db.relationship('Item', backref='department')
    
    def __repr__(self):
        return '<Dept - %s>' % self.name

# ========================================
#                  ITEM
# ========================================

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # belongs_to
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    # has_many
    list_items = db.relationship('ListItem', backref='item')


    def __repr__(self):
        return '<Item - %s - %s>' % (self.name, self.department.name)

# ========================================
#                LIST ITEM
# ========================================

class ListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    # belongs_to
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)

    @property
    def name(self):
        item = Item.query.filter_by(id = self.item_id).first()
        return item.name

    def __repr__(self):
        return '<ListItem - %s - %s>' % (self.item.name, self.quantity)



