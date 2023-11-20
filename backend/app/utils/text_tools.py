from sklearn.metrics.pairwise import cosine_similarity
import re


def clean_text(text):
    text = re.sub(r'\.\w+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    return text

def predict(text,resources):
    query_vec = resources.vectorizer.transform([text])
    similarity = cosine_similarity(query_vec, resources.description_vectors).flatten()
    result_ids = similarity.argsort()[:-11:-1]
    results = [resources.ids_descriptions.get(img_id).split("app/")[1] for img_id in result_ids]
    return results