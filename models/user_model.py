from db import db 
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(80), primary_key = True)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(100), nullable=True,default = "sin_nombre")
    token = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(),default = datetime.now())

