from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from PIL import Image
import json
import numpy as np 
from app import app,Image

def clean_text(text):
    text = re.sub(r'\.\w+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    return text


def load_all_images():
    with app.app_context():
        images=Image.query.all()
        corpus=[image.description for image in images]
        ids_descriptions={idx:image.path for idx,image in enumerate(images)}
    return corpus,ids_descriptions

corpus,ids_descriptions=load_all_images()

vectorizer = TfidfVectorizer()
description_vectors = vectorizer.fit_transform(corpus)

pattern=r'[^a-zA-Z0-9]'


def predict(text):
    query_vec = vectorizer.transform([text])
    similarity = cosine_similarity(query_vec, description_vectors).flatten()
    result_ids = similarity.argsort()[:-11:-1]
    results=[ids_descriptions.get(img_id) for img_id in result_ids]
    return results

