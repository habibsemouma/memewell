from app import app,db,User,Image,request,jsonify,send_from_directory,backend_uri
from utils import clean_text,pattern,vectorizer,predict

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


if __name__ == "__main__":
    app.run()