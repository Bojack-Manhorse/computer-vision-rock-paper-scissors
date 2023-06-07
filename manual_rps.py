import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_user_choice():
    choice = input("Choose rock, paper or scissors")
    if choice not in ["Rock", "Paper", "Scissors"]:
        print("Incorrect choice, try again!")
        get_user_choice()
    return choice


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
        return
    elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
        print("You won!")
        return
    else:
        print("You lost!")

def play():
    get_winner(get_computer_choice(), get_user_choice())