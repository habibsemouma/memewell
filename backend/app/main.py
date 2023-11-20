from resources import resources
from flask import request, jsonify,send_from_directory
from werkzeug.utils import secure_filename
from utils.img_tools import load_all_images
from utils.text_tools import clean_text,predict
from sklearn.feature_extraction.text import TfidfVectorizer
import os

corpus,ids_descriptions=load_all_images(resources)
vectorizer= TfidfVectorizer()
description_vectors=vectorizer.fit_transform(corpus)
resources.register_txt_tools(ids_descriptions,corpus,vectorizer,description_vectors)

static=os.path.abspath("dump")

@resources.app.route('/dump/<path:filename>')
def static_files(filename):
    return send_from_directory("/home/habib/websites/AI-meme-archive/backend/app/dump", filename)


@resources.app.route("/images_fetch",methods=["POST"])
def images_fetch():
    data=request.get_json()
    text=clean_text(data.get("text"))
    prefix=clean_text(data.get("prefix"))
    images_paths=predict(f"{prefix} {text}",resources)
    data={"images":[f"{resources.env_vars.get('backend_uri')}/{path}" for path in images_paths]}
    return jsonify(data)

@resources.app.route("/images_add",methods=["POST"])
def image_add():
    data=request.form
    img=request.files.get("img")
    description=clean_text(data.get("description"))
    if img and allowed_file(img.filename):
        filename=secure_filename(img.filename)
    path=f"dump/memes/twitterfr/{filename}"
    i = Image.open(io.BytesIO(img.read()))

    width, height = i.size
    if width <= 500 and height <= 500:
        pass
    else:
        new_width = 500
        new_height = 500
        i = i.resize((int(new_width), int(new_height)))
        i.save(path)
    return jsonify({"message":"image added succesfully"})


if __name__ == "__main__":
    resources.app.run()