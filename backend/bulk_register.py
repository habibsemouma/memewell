from PIL import Image as Image_module
import os
import shutil
from app import Image, db,app

def delete_empty_subfolders(folder):
  for root, dirs, files in os.walk(folder, topdown=False):
    if not dirs and not files:
      print(f"Deleting empty folder: {root}")
      os.rmdir(root)



def resize_img(path):
    i = Image_module.open(path)

    width, height = i.size
    if width <= 500 and height <= 500:
        pass
    else:
        new_width = 500
        new_height = 500
        i = i.resize((int(new_width), int(new_height)))
    i.save(path)


src_folder = 'dump/added'
dst_folder = 'dump/memes'
moved=[]
with app.app_context():
    for root, dirs, files in os.walk(src_folder):
        for f in files:
            if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
                path = os.path.join(root, f)
                try:
                    resize_img(path)
                    new_path = path.replace("added/", "memes/")
                    image = Image(description=f, path=new_path)
                    db.session.add(image)
                    moved.append([path,root.replace("added/","memes/")])
                except:
                    print(f"error for {path}")
    db.session.commit()

for paths in moved:
    shutil.move(paths[0],paths[1])
delete_empty_subfolders(src_folder)