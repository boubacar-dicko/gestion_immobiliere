from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    biens = db.relationship('Bien', backref='user')
    def __repr__(self):
        return '<User %r>' % self.username
    
    @property
    def password(self):
        raise Exception('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


# class Client(db.Model):
#     __tablename__ = 'clients'
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(64), unique=False)
#     lastname = db.Column(db.String(64), unique=False)
#     adresse = db.Column(db.String(64))
#     telephone = db.Column(db.String(64), unique=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     def __repr__(self):
#         return '<Client %r>' % self.firstname

# class Proprietaire(db.Model):
#     __tablename__ = 'proprietaires'
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(64), unique=False)
#     lastname = db.Column(db.String(64), unique=False)
#     adresse = db.Column(db.String(64))
#     email = db.Column(db.String(64), unique=False)
#     telephone = db.Column(db.String(64), unique=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     biens = db.relationship('Bien', backref='proprietaire')
#     def __repr__(self):
#         return '<Proprietaire %r>' % self.firstname

class Bien(db.Model):
    __tablename__ = 'biens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    typeBien = db.Column(db.String(64), unique=False)
    adresseBien = db.Column(db.String(64), unique=False)
    firstname = db.Column(db.String(64), unique=False)
    lastname = db.Column(db.String(64), unique=False)
    adresse = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=False)
    telephone = db.Column(db.String(64), unique=True)
    descriptionBien = db.Column(db.Text(200), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __repr__(self):
        return '<Bien %r>' % self.name