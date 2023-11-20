import os
from utils.text_tools import clean_text
import json
def create_json(src,dst):
    memes = {
        "description": [], "path": []
    }
    for category in os.listdir(src):
        path = f"{src}/{category}"
        for meme in os.listdir(path):
            memes["description"].append(clean_text(f"{category} {meme}")),
            memes["path"].append(f"{src}/{category}/{meme}")

    with open(f"{dst}/memes.json", "w") as f:
        f.write(json.dumps(memes))

    return memes


def create_db(resources):
    resources.db.create_all()

def populate_db(resources):
    memes=json.loads(open(f"{resources.folders.get('dump_folder')}/memes.json",'r').read())
    Image=resources.models.get("Image")
    for description, path in zip(memes["description"], memes["path"]):
        image = Image(description=description, path=path)
        resources.db.session.add(image)
    resources.db.session.commit()


def fetch_db(resources):
    Image=resources.models.get('Image')
    with resources.app.app_context():
        images = Image.query.all()
        for image in images:
            print(image.path, image.description)
            break


def drop_db(resources):
    Image=resources.models.get('Image')
    with resources.app.app_context():
        Image.query.delete()
        resources.db.session.commit()


