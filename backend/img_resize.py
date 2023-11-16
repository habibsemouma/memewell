import os
from PIL import Image

for root, dirs, files in os.walk('memes'):

    for f in files:

        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            path = os.path.join(root, f)
            try:
                i = Image.open(path)

                width, height = i.size
                if width == 500 and height == 500:
                    continue
                else:
                    new_width = 500
                    new_height = 500

                i = i.resize((int(new_width), int(new_height)))

                i.save(path)
            except:print(f"error for {path}")
