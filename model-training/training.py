from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app import db,app,User,Image
import numpy as np

with app.app_context():
    images=Image.query.all()
    texts=[image.description for image in images]
    ids_descriptions={idx:image.path for idx,image in enumerate(images)}

vectorizer = TfidfVectorizer()
description_vectors = vectorizer.fit_transform(texts)

def search_descriptions(query):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, description_vectors).flatten()
    related_docs_indices = similarity.argsort()[:-11:-1]
    return [texts[i] for i in related_docs_indices]


user_query = "spongebob dumb"
results = search_descriptions(user_query)
print(results)
