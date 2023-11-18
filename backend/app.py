from flask import Flask, request, jsonify, send_from_directory,secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from PIL import Image
import json
import numpy as np
import sys
import io

app = Flask("memesapp")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI")
backend_uri = os.environ.get("BACKEND_URI")
app.config['STATIC_FOLDER'] = 'memes'
whitelist = os.environ.get('CORS_ALLOWED')
CORS(app, origins=whitelist)
db = SQLAlchemy(app)


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


def clean_text(text):
    text = re.sub(r'\.\w+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    return text


def load_all_images():
    with app.app_context():
        images = Image.query.all()
        corpus = [image.description for image in images]
        ids_descriptions = {idx: image.path for idx,
                            image in enumerate(images)}
    return corpus, ids_descriptions


def predict(text):
    query_vec = vectorizer.transform([text])
    similarity = cosine_similarity(query_vec, description_vectors).flatten()
    result_ids = similarity.argsort()[:-11:-1]
    results = [ids_descriptions.get(img_id) for img_id in result_ids]
    return results

try:
    corpus, ids_descriptions = load_all_images()
    vectorizer = TfidfVectorizer()
    description_vectors = vectorizer.fit_transform(corpus)
except:print("Database not loaded yet")