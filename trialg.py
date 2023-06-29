import random

def get_choices():
    player_choice=input("Enter a choice(Rock,Paper,Siccors)\n")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player": player_choice,"computer": computer_choice}
    return choices


def check_win(player,computer):
    print(f"You chose :{player}\nComputer chose :{computer}")
    if player==computer:
        return "Its a tie."
    
    elif player=="rock":
        if computer=="paper":
            return "You lose."
        else:
            return "You win."
    
    elif player=="paper":
        if computer=="scissors":
            return "You lose"
        else:
            return "You win."
 
    elif player=="scissors":
        if computer=="rock":
            return "You lose."
        else:
            return "You win"

choices=get_choices()
print(check_win(choices["player"],choices["computer"]))

input()