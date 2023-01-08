print("="*50, "MAGIC NUMBER", "="*50)
print("I have a number between 1 and 10. Can you guess it?")

lifes = 3
magic_number = 5
player_guess = input("Your number?")

while player_guess != str(magic_number):
    lifes -= 1
    if lifes == 0:
        print("You lost this game. Maybe next time :(")
        exit()

    print(f"Wrong guess :( Try again. You have {lifes} lifes left.")
    player_guess = input("Your number?")

print(f"That's right! {magic_number} was my number! :)))")