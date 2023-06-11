import RPS_Template_in_function as rps
import random

class RPSGame:
    """
    The RPSGame class takes in 2 parameters, the number of wins needed to finish and the length of time the webcam display is up for
    """
    def __init__(self, num_wins, delay = 5):
        self.num_wins = num_wins
        self.delay = max(5, delay)
        self.user_choice = ""
        self.computer_choice = ""

    possibilities = ["Rock", "Paper", "Scissors"]

    def get_prediction(self):
        """
        get_prediction runs the function from "RPS_Template_in_funciton" to use to webcam to get an out of rock, paper or scissors, and assigns self.user_choice to it.
        If no input was detected, it will choose one at random.
        """
        model_output = rps.get_input(self.delay)

        for i in range(4):
            if model_output[i] > 0.6 and i < 3:
                self.user_choice = self.possibilities[i]
                
            if i == 3:
                print("You didn't choose anything! Choosing at random")
                self.user_choice = random.choice(self.possibilities)

        print(f"You chose {self.user_choice}")
            
    def get_computer_choice(self):
        """
        get_computer_choice makes a choice for the computer and sets self.computer_choice equal to it.
        """
        self.computer_choice = random.choice(self.possibilities)
        print(f"Computer chose {self.computer_choice}")

    def get_winner(self, user_choice, computer_choice):
        """
        This function decided a winner of rock paper scissors given two inputs. It returns +1 if the user_choice player wins, else returns 0
        """
        
        if computer_choice == user_choice:
            print("It is a tie!")
            return 0
        elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
            print("You won!")
            return 1
        else:
            print("You lost!")
            return 0
        
    def play_until_num_wins(self):
        """
        Keeps playing rock paper scissors until the player wins self.num_wins times.
        """
        win_count = 0
        input(f"We'll play Rock Paper Scissors until you win {self.num_wins} times, press enter to begin!")
        while win_count < self.num_wins:
            self.get_prediction()
            self.get_computer_choice()
            win_count += self.get_winner(self.user_choice, self.computer_choice)
            if win_count < self.num_wins:
                str = "s"
                input(f"You have won {win_count} time{str * bool(not win_count == 1)}, press enter to continue.")
            else:
                print("Congratulations, you have won!")
                break


def start_script():
    """
    script to start playing rock paper scissors.
    """
    user_input = input("Please enter how many games you would like to play")
    
    try:
        number_of_games = int(user_input)
        assert number_of_games > 0
        return number_of_games
    except:
        raise Exception("That's not a positive integer")
    

my_game = RPSGame(start_script())
my_game.play_until_num_wins()




