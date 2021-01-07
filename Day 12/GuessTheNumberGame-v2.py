from random import randint
from art import logo

def set_difficulty():
    '''A function which returns the number of attempts associated with the chosen difficulty'''
    if input("Choose a difficulty. Type 'easy' or 'hard': \n").lower() == "hard":
        return 5
    else:
        return  10 

def answer_checker(guess, answer, turns):
    '''A function to compare the user's guess against the answer and print the appropritate text.'''   
    
    if answer < guess:
        print("Too high. \nGuess Again.")
        return turns - 1
    elif answer > guess:
        print("Too low. \nGuess Again.")   
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    # Print intro text
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Choose number & difficulty
    rand_num = randint(1, 100)
    attempts_left = set_difficulty()

    guessed_num = 0
    # Loop through the game
    while guessed_num != rand_num:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        
        guessed_num = int(input("Make a guess: "))
        
        attempts_left = answer_checker(guessed_num, rand_num, attempts_left)
        if attempts_left == 0:
            print("You've run out of guesses, you lose.")
            return
            #The return ends the function(and therefore the while loop) and returns the print.
        elif guessed_num != rand_num:
            print("Guess again.")


game()
