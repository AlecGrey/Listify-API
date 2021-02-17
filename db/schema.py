from run import ma

# ========================================
#                 LIST
# ========================================

class ListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date')

# Initialize User Schema
list_schema = ListSchema()
lists_schema = ListSchema(many=True)

# ========================================
#                 USER
# ========================================

class UserSchema(ma.Schema):
    lists = ma.Nested(ListSchema, many=True)

    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email', 'lists')

# Initialize User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)