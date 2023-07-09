import random
import time

while True:
    computer = ["rock","paper","scissors"]
    computerChoice = random.choice(computer)
    player = None
    win = False
    draw = False
    drawText = "this is a draw"
    computerWinText = "computer win"
    playerWinText = "player win"

    while player not in computer:
        player = str(input("rock paper or scissors: "))
        player.lower()
        time.sleep(1)
        print("loading....")
        time.sleep(2)
    print("computer choose: "+computerChoice)

    if player == "rock" and computerChoice == "scissors":
        win = True
        print(playerWinText)
    elif player == "paper" and computerChoice == "rock":
        win = True
        print(playerWinText)
    elif player == "scissors" and computerChoice == "paper":
        win = True
        print(playerWinText)
    elif computerChoice == "rock" and player == "scissors":
        win = True
        print(computerWinText)
    elif computerChoice == "paper" and player == "rock":
        win = True
        print(computerWinText)
    elif computerChoice == "scissors" and player == "paper":
        win = True
        print(computerWinText)
    else:
        draw = True
        print(drawText)
        
    quit = str(input("do you want to play again?(yes/no): ")).lower()
    if quit == "no":
        break
    elif quit != "no":
        print("you have choose to play again")