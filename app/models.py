from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(64))
    last = db.Column(db.String(64))
    dob = db.Column(db.Date)
    street_addr1 = db.Column(db.String(64))
    street_addr2 = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(9))
    gender = db.Column(db.Enum('M', 'F'))
    home_box = db.Column(db.String(32))
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Competition(db.Model):
    __tablename__ = 'competitions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    #price = db.Column(db.Numeric)
    #category = db.Column(db.Enum(['men', 'women', 'masters']))
    #start_datetime = db.Column(db.Date)
    #end_datetime = db.Column(db.Date)

