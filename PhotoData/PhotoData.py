import os, json
from PIL import Image, ExifTags

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

# read image data
for image_file in photo_files:
    img = Image.open(image_file)

    size = img.size
    exif_data = img._getexif()
    if not exif_data:  # skip images without exif data
        continue

    camera_model = exif_data.get(0x0110)
    date = exif_data.get(0x9003)
    iso = exif_data.get(0x8827)

    #print(image_file, size, camera_model, date, iso)

phonebook = {
    "06 20 123 4567": "Robert",
    "06 30 987 4538": "Csaba"
}

with open("phonebook.json", "w") as data_file:
    json.dump(phonebook, data_file)