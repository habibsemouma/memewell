from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
import json


app = Flask("memesapp")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
whitelist = os.environ.get('CORS_ALLOWED')
CORS(app, origins=whitelist)
db=SQLAlchemy(app)


folders = {"memes_folder": os.path.abspath("dump/memes"),
               "dump_folder": os.path.abspath("dump"),
               "added_folder": os.path.abspath("dump/added")}
env_vars={
        "backend_uri":os.environ.get("BACKEND_URI")
    }





class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, path, description):
        self.path = path
        self.description = description


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)
    request_content = db.Column(db.Text, nullable=True)

models={
    "Image":Image,
    "User":User
}



class AppResources():
    def __init__(self,app,db,models,folders,env_vars):
        self.app=app
        self.env_vars=env_vars
        self.folders=folders
        self.Image_class=Image
        self.db=db
        self.models=models
    def register_txt_tools(self,ids_descriptions,corpus,vectorizer,description_vectors):
        self.ids_descriptions=ids_descriptions
        self.corpus=corpus
        self.description_vectors=description_vectors
        self.vectorizer=vectorizer

    def allowed_image(self,filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        flag='.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        return flag
    def allowed_video(self,filename):
        ALLOWED_EXTENSIONS = {"mp4", "avi", "mov"}
        flag='.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        return flag


resources=AppResources(app,db,models,folders,env_vars)




