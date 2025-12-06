from random import randint
print("Rock....")
print("Paper....")
print("Scissor....")

print()

player = input("player make your move ").lower()

rand_number = randint(0,2)
if rand_number == 0:
        computer = "rock"
elif rand_number == 1:
        computer = "paper"
else:
        computer = "scissor"
print(f"computer playes, {computer} ")

print()


# player2 = input("player2 make your move ").lower()

if player == "rock" and computer == "scissor":
        print("player wins")
elif player == "rock" and computer == "paper":
        print("computer wins")
elif player == "paper" and computer == "rock":
        print("player wins")
elif player == "paper" and computer == "scissor":
        print("computer wins")
elif player == "scissor" and computer == "rock":
        print("computer wins")
elif player == "scissor" and computer == "paper":
        print("player wins")
elif player == computer:
        print("It's tie")
else:
        print("Please enter valid move.")

                               