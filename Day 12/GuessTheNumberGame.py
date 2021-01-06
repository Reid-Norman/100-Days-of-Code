import random 
import art

def answer_checker(guess, answer):
    '''A function to compare the user's guess against the answer and print the appropritate text. This will also end the game if the correct answer is inputted'''
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        global game_over
        game_over = True    
    elif answer < guess:
        print("Too high. \nGuess Again.")
    elif answer > guess:
        print("Too low. \nGuess Again.")    

# Choose number
rand_num = random.randint(1, 101)

# Print intro text
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {rand_num}")

# Choose attempt number/ difficulty
if input("Choose a difficulty. Type 'easy' or 'hard': \n").lower() == "hard":
    attempts_left = 5
else:
    attempts_left = 10 

# Loop through the game
game_over = False
while not game_over:
    print(f"You have {attempts_left} attempts remaining to guess the number.")

    guessed_num = int(input("Make a guess: "))
    if guessed_num != rand_num:
        attempts_left -= 1
        if attempts_left == 0:
            print("You've run out of guesses, you lose.")
            game_over = True

    answer_checker(guessed_num, rand_num)

