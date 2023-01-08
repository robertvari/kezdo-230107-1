import os
from PIL import Image

# r = raw string
folder_path = r"D:\Work\_PythonSuli\kezdo-230107\photos"

# check if path exists
assert os.path.exists(folder_path), f"The path: {folder_path} doesn't exist :((("

# check if this is a folder
assert os.path.isdir(folder_path), f"The path: {folder_path} must be a directory. :((("

# load files and folders from folder_path
folder_content = os.listdir(folder_path)

# todo: filter folder content. Only .jpg files allowed!
alowed_extensions = ["jpg", "jpeg"]

# filter folder_content and collect .jpg and .jpeg files
photo_files = []
for item in folder_content:
    full_path = os.path.join(folder_path, item)
    
    # todo skip folders
    if os.path.isdir(full_path):
        continue

    item_list = item.lower().split(".")
    extension = item_list[-1]

    if extension in alowed_extensions:
        photo_files.append(full_path)