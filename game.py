# Rock Paper Scissor.
print("Rock....")
print("Paper....")
print("Scissor....")

player1 = input("player1 make your move ").lower()

player2 = input("player2 make your move ").lower()

if player1 == "rock" and player2 == "scissor":
        print("player1 wins")
elif player1 == "rock" and player2 == "paper":
        print("player2 wins")
elif player1 == "paper" and player2 == "rock":
        print("player1 wins")
elif player1 == "paper" and player2 == "scissor":
        print("player2 wins")
elif player1 == "scissor" and player2 == "rock":
        print("player2 wins")
elif player1 == "scissor" and player2 == "paper":
        print("player1 wins")
elif player1 == player2:
        print("It's tie")
else:
        print("Something went wrong")

                               