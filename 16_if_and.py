import getpass

username = "robert"
password = "testpas123"

username_input = input("Username?")
password_input = getpass.getpass("Password?")

print("User password:", password_input)
#            True                             True
if (username == username_input) and (password == password_input):
    print(f"Hello {username}. How are you today?")
else:
    print("username or password is incorrect. Try again.")