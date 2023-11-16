import re
import os
import json


def clean_text(text):
    text = re.sub(r'\.\w+', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    return text


folder = "memes"


memes = {
     "description":[],"path":[]
}
for category in os.listdir(folder):
    path = f"{folder}/{category}"
    for meme in os.listdir(path):
          memes["description"].append(clean_text(f"{category} {meme}")),
          memes["path"].append(f"{folder}/{category}/{meme}") 


with open("memes.json", "w") as f:
    f.write(json.dumps(memes))
