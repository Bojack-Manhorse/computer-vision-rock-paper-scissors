import RPS_Template_in_function as rps
import random
import time
import manual_rps

possibilities = ["Rock", "Paper", "Scissors", "Nothing"]


def get_prediction():
    model_output = rps.get_input(5)

    for i in range(4):
        if model_output[i] > 0.6 and i < 3:
            print(f"You chose {possibilities[i]}")
            return(possibilities[i])
            break
        if i == 3:
            print("You didn't choose anything! Choosing at random")
            choice = random.choice(["Rock", "Paper", "Scissors"])
            print(f"You choice is {choice}")
            return choice

def play_until_num_wins(num_of_wins):
    win_count = 0
    while win_count < num_of_wins:
        win_count += manual_rps.get_winner(get_prediction(), manual_rps.get_computer_choice())
        print(f"You have won {win_count} times")

#rps.get_input(3)

#get_prediction()

play_until_num_wins(3)




