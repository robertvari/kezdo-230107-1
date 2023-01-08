import json

phonebook = {
    "06 20 123 4567": "Robert",
    "06 30 987 4538": "Csaba"
}

# write out a dictionary to a .json file
with open("phonebook.json", "w") as data_file:
    json.dump(phonebook, data_file)


# read .json from disk
with open("phonebook.json") as data_file:
    my_data = json.load(data_file)
    print(my_data)

with open("phonebook.txt", "w") as data_file:
    data_file.write(str(phonebook))