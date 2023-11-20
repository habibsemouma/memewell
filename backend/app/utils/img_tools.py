import os
from PIL import Image as Image_module

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


def delete_empty_subfolders(folder):
  for root, dirs, files in os.walk(folder, topdown=False):
    if not dirs and not files:
      print(f"Deleting empty folder: {root}")
      os.rmdir(root)

def register_image(img_path,root,resources):
    Image=resources.models.get("Image")
    if img_path.endswith('.jpg') or img_path.endswith('.jpeg') or img_path.endswith('.png'):
        path = os.path.join(root, img_path)
        try:
            resize_img(path)
            new_path = path.replace("added/", "memes/")
            image = Image(description=img_path, path=new_path)
            resources.db.session.add(image)
            return new_path
        except Exception as e:
            print(f"error for {path} {e}")
            return None
        


def load_all_images(resources):
    Image=resources.models.get('Image')
    with resources.app.app_context():
        images = Image.query.all()
        corpus = [image.description for image in images]
        ids_descriptions = {idx: image.path for idx,
                            image in enumerate(images)}
    return corpus, ids_descriptions