#rock_paper_scissor project 

import random

def play_game(player_input):
    game_list = ["rock","paper","scissor"]
    computer_input = random.choice(game_list)
    print(f"computer selected {computer_input}")

    if (player_input==computer_input):
        print("game is draw")
    elif(player_input=="rock" and computer_input=="paper"):
        print("computer won")
    elif(player_input=="paper" and computer_input=="scissor"):
        print("computer won")
    elif(player_input=="scissor" and computer_input=="rock"):
        print("compter won")
    else:
        print("you won")
    

player_input = (input("enter either Rock or Paper or Scissor as your input to play the game: ")).lower()
game_list = ["rock","paper","scissor"]
if(player_input in game_list):
    play_game(player_input)
else:
    print("you have entered invalid input restart the game")