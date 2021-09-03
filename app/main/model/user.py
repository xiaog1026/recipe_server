from .. import db, flask_bcrypt




class User(db.Model):
    """
    User is not account.
    user to dish is 1 to many
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=False)
    password = db.Column(db.String(50))
    registered_on = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return "<User '{}'>".format(self.username)