from app import db, app, Image,clean_text
import json
import os
import re

def create_json():
    folder = "dump/memes"
    memes = {
        "description": [], "path": []
    }
    for category in os.listdir(folder):
        path = f"{folder}/{category}"
        for meme in os.listdir(path):
            memes["description"].append(clean_text(f"{category} {meme}")),
            memes["path"].append(f"{folder}/{category}/{meme}")

    with open("memes.json", "w") as f:
        f.write(json.dumps(memes))

    return memes


def create_db():
    with app.app_context():
        db.create_all()

def populate_db():
    with app.app_context():

        for description, path in zip(memes["description"], memes["path"]):
            image = Image(description=description, path=path)
            db.session.add(image)

        db.session.commit()


def fetch_db():
    with app.app_context():
        images = Image.query.all()
        for image in images:
            print(image.path, image.description)
            break


def drop_db():
    with app.app_context():
        Image.query.delete()
        db.session.commit()


try:
    drop_db()
except:
    pass
memes=create_json()
create_db()
populate_db()
print("database loaded")
