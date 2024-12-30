# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.

from random import randint

computer_random_no = randint(0,100)
user_attempt = 0
user_guess = None
print ("Computer has generated one random number between 0-100 including both the endpoints, Please try to guess it..")
while (user_guess != computer_random_no):
    user_guess = int (input("guess the number now: "))
    user_attempt +=1
    if(user_guess == computer_random_no):
        print (f"""you have correctly guessed the number within {user_attempt} attempts. 
               Computer had randomly generated {computer_random_no} """)
        break
    elif(user_guess<computer_random_no):
        print("your guess was less than the computer's number.")
    else:
        print("your guess was higher than the computer's number.")
