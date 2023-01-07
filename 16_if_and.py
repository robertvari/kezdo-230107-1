username = "robert"
password = "testpas123"

username_input = input("Username?")
password_input = input("Password?")

if username == username_input and password == password_input:
    print(f"Hello {username}. How are you today?")
else:
    print("username or password is incorrect. Try again.")