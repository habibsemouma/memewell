from flask import Flask,request,jsonify,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

app=Flask("memesapp")

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DB_URI")
backend_uri=os.environ.get("BACKEND_URI")
app.config['STATIC_FOLDER'] = 'memes'
whitelist=os.environ.get('CORS_ALLOWED')
print(whitelist)
CORS(app,origins=whitelist)

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