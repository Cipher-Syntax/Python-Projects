import sys
import random
print("================================================")
print(f"{"Rock Paper Scissor":^50}")
print("================================================")
wins = 0
losses = 0
ties = 0

while True:
    print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
    print("================================================")
    print("Enter your move...")
    player = input("(r) - rock, (p) - paper, (s) - scissor or 'q' to quit: ").lower()

    if player == "r":
        print("================================================")
        print("Rock Versus", end=" ")
    elif player == "p":
        print("================================================")
        print("Paper versus", end=" ")
    elif player == "s":
        print("================================================")
        print("Scissors versus", end=" ")
    elif player == "q":
        sys.exit()
    
    random_num = random.randint(1,3)

    if random_num == 1:
        computer = "r"
        print("Rock")
    elif random_num == 2:
        computer = "p"
        print("Paper")
    elif random_num == 3:
        computer = "s"
        print("Scissor")

    if player == computer:
        print("Its a Tie")
        ties += 1
    elif player == "r" and computer == "s":
        print("You Win")
        wins += 1
    elif player == "p" and computer == "r":
        print("You Win")
        wins += 1
    elif player == "s" and computer == "p":
        print("You Win")
        wins += 1
    elif player == "r" and computer == "p":
        print("You Lose")
        losses += 1
    elif player == "p" and computer == "s":
        print("You Lose")
        losses += 1
    elif player == "s" and computer == "r":
        print("You Lose")
        losses += 1
    
    

