car_registry = {
    "ABC-123": {"name":"Kriszta", "address": "Pécs", "phone":"06 20 543 6754"},
    "FGR-543": {"name":"Csaba", "address": "Budapest", "phone":"06 20 123 7568"},
    "RGE-585": {"name":"Tamás", "address": "Miskolc", "phone":"06 30 876 9258"},
    "NGD-765": {"name":"Csilla", "address": "Debrecen", "phone":"06 30 435 7874"},
}

# get data from dictionary
print(car_registry["FGR-543"]["address"])

# get keys or values from a dict
print(car_registry.keys())
print(car_registry.values())

# add new item to a dictionary
car_registry["HGF-936"] = {"name":"Laci", "address": "Pécs", "phone":"06 20 484 6254"}

# delete item from dictionary
del car_registry["HGF-936"]

# update item in dictionary
car_registry["ABC-123"] = {"name":"Géza", "address": "Debrecen", "phone":"06 30 999 6754"}
car_registry["ABC-123"]["address"] = "Bécs"

print(car_registry["ABC-123"])