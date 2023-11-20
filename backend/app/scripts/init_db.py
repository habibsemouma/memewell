import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.db_tools import create_db,create_json,populate_db
from resources import resources

src=resources.folders.get("memes_folder")
dst=resources.folders.get("dump_folder")

with resources.app.app_context():
    create_db(resources)
    memes=create_json(src,dst)
    populate_db(resources)
