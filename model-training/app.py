from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask("memesapp")

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DB_TEST_URI")
db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String,nullable=False)

    def __init__(self, path, description):
        self.path = path
        self.description = description

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    request_content = db.Column(db.Text, nullable=True)