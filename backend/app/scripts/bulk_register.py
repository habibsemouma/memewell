import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from resources import resources
import shutil
from utils.img_tools import register_image,delete_empty_subfolders

src_folder=resources.folders.get("added_folder")
dst_folder=resources.folders.get("memes_folder")

moved=[]
with resources.app.app_context():
    for root, dirs, files in os.walk(src_folder):
        for img_path in files:
            path=register_image(img_path,root,resources)
            if path is not None:
                moved.append(path)
    resources.db.session.commit()


for img_path in moved:
    shutil.move(img_path,dst_folder+"/twitterfr/")


delete_empty_subfolders(src_folder)


