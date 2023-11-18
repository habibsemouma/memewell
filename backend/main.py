from app import app,db,User,Image,request,jsonify,send_from_directory,backend_uri,clean_text,pattern,vectorizer,predict,secure_filename,io


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/memes/<path:filename>')
def static_files(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)

@app.route("/images_fetch",methods=["POST"])
def images_fetch():
    data=request.get_json()
    text=clean_text(data.get("text"))
    prefix=clean_text(data.get("prefix"))
    images_paths=predict(f"{prefix} {text}")
    data={"images":[f"{backend_uri}/{path}" for path in images_paths]}
    return jsonify(data)

@app.route("/images_add",methods=["POST"])
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
        continue
    else:
        new_width = 500
        new_height = 500
        i = i.resize((int(new_width), int(new_height)))
        i.save(path)
    return jsonify({"message":"image added succesfully"})


if __name__ == "__main__":
    app.run()