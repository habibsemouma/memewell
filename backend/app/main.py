from resources import resources
from flask import request, jsonify,send_from_directory
from werkzeug.utils import secure_filename
from utils.img_tools import load_all_images,dump_image,resize_img,Image_module
from utils.text_tools import clean_text,predict
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re
import io

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

@resources.app.route("/image_add",methods=["POST"])
def image_add():

    data=request.form
    img=request.files.get("image")
    description=clean_text(data.get("description"))


    if img and resources.allowed_file(img.filename):
        filename=secure_filename(img.filename)
    else: 
        message="Error try again later"
        return jsonify({"message":message})
        
    extension = re.search("(?<=\.)\w+$", filename).group(0)
    folder=resources.folders.get("added_folder")
    path=f"{folder}/{description}.{extension}"

    image = Image_module.open(io.BytesIO(img.read()))
    message=dump_image(image,path)
    return jsonify({"message":message})


@resources.app.route("/video_add",methods=["POST"])
def video_add():

    data=request.form
    img=request.files.get("video")
    description=clean_text(data.get("description"))


    if vid and resources.allowed_file(vid.filename):
        filename=secure_filename(vid.filename)
    else: 
        message="Error try again later"
        return jsonify({"message":message})
        
    extension = re.search("(?<=\.)\w+$", filename).group(0)
    folder=resources.folders.get("added_folder")
    path=f"{folder}/{description}.{extension}"

    image = Image_module.open(io.BytesIO(vid.read()))
    message=dump_image(image,path)
    return jsonify({"message":message})


if __name__ == "__main__":
    resources.app.run()