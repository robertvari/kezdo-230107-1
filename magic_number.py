print("="*50, "MAGIC NUMBER", "="*50)
print("I have a number between 1 and 10. Can you guess it?")

magic_number = 5
player_guess = input("Your number?")

while player_guess != str(magic_number):
    print("Wrong guess :( Try again")
    player_guess = input("Your number?")

print(f"That's right! {magic_number} was my number! :)))")