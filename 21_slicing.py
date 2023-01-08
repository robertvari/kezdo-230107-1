import random

my_friends = [
    "kriszta", 
    "csaba", 
    "csilla", 
    "zoli", 
    "Betty", 
    "Nicole", 
    "Sapphire", 
    "Madiha"
]

# my_list[START_INDEX : STOP_INDEX : STEP]
print(my_friends[:3])

for name in my_friends[3:]:
    print(name)


# slicing works with strings
my_name = "Robert Vari"
print(my_name[::2])