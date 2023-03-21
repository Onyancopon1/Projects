import easygui
import random

while True:
    hand=["Paper","scissors","Rock"]
    computer=random.choice(hand)
    play_again=easygui.buttonbox("Welcome to Rock,Paper,Scissors\n\n"
                                 "Rock beats Scissors\n"
                                 "Scissors beats Paper\n"
                                 "Paper beats Rock\n"
                                 "Do you want to play\n"
                                 "Welcome and Rules", choices=["Yes","No"])
    if play_again=="No":
        break
    else:
        player=easygui.buttonbox("Choose your weapon","Choose weapon",
                                 choices=[hand[0],hand[1],
                                          hand[2]])
        easygui.msgbox(f"You chose {player}and the computer"
                       f"choose{computer}", "Choice")

        if computer == player:
            result = "This was a draw"
        elif computer =="Paper" and player == "Rock" or computer == "Scissors"\
                and player == "Paper" or computer == "Rock" and player == "Scissors":
            result ="You lose"
        else:
            result="You win"

        easygui.msgbox(f"{result}")
    print("Goodbye")

