import os

# r = raw string
folder_path = r"D:\Work\_PythonSuli\kezdo-230107\photos\IMG_1070.JPG"

# check if path exists
assert os.path.exists(folder_path), f"The path: {folder_path} doesn't exist :((("

# check if this is a folder
assert os.path.isdir(folder_path), f"The path: {folder_path} must be a directory. :((("

# load files and folders from folder_path
files = os.listdir(folder_path)

for i in files:
    print(i)