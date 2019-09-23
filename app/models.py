from werkzeug.security import check_password_hash

from app.exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password =db.Column(db.String(128))

    def check_password(self, password):

        return check_password_hash(self.password,password)


class Edit(db.Model):
    __tablename__ = 'edit'
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    datetime = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',backref=db.backref('edits'))