import random
secret_number = random.randint(0, 10)

for guess in range(1, 6):
    number = int(input(f"I am thinking a number between (0 - 10): "))
    if number < secret_number:
        print("Your guess is too low")
    elif number > secret_number:
        print("Your Guess is too high")
    else:
        break

if secret_number == number:
    print(f"You guess right....congratulations...it took you {guess} times to guess")
else:
    print(f"meh...I was thinking the number {secret_number}")