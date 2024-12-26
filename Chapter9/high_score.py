# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score.
# You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random

def game():
    return random.randint(1,100)

game_score = game()
with open("high_score.txt") as content: # difficult to do both read and write operation in one open command 
    content_read = content.read()       # as we just need one single value in the file which high score. 
    if (content_read == ""):
        file_old_score=0
    else:
        file_old_score=int(content_read)
    
with open("high_score.txt","w") as content:   
    if (game_score > file_old_score):
        content.truncate(0)
        content.write(str(game_score)) #only string content can be written to the file
        print(f"new high score {game_score} has been updated in the file")
    else:
        content.write(str(file_old_score)) # have to update old score again the file as file gets truncated when you open the file in write mode
        print(f"your game score {game_score} is less than high score {file_old_score}" ) 


