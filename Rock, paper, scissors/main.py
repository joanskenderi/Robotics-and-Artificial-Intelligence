# Write a rock, paper, scissors game using Python.

import random

player = input("Pick rock, paper or scissors: ")
player = player.lower()

random.seed()

while True:
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        computer = "rock"
        break
    elif computer_choice == 1:
        computer = "scissors"
        break
    elif computer_choice == 2:
        computer_choice = "paper"
        break

print("Computer chose: ", computer)
print("Player chose: ", player)

if player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("Computer wins!")
    elif computer == "paper":
        print("It is a tie.")
elif player == "rock":
    if computer == "rock":
        print("It is a tie.")
    elif computer == "scissors":
        print("Player wins!")
    elif computer == "paper":
        print("Computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins!")
    elif computer == "scissors":
        print("It is a tie.")
    elif computer == "paper":
        print("Player wins!")
else:
    print("You did not choose a valid option.")
