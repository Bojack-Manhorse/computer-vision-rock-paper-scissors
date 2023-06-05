import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Choose rock, paper or scissors")
    if choice not in ["rock", "paper", "scissors"]:
        print("Incorrect choice, try again!")
        get_user_choice()
    return choice

#get_user_choice()

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
        return
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        print("You won!")
        return
    else:
        print("You lost!")

get_winner(get_computer_choice(), get_user_choice())