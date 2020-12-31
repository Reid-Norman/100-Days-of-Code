#Completed Hangman Game

import random
import hangman_words
import hangman_art
#You can also...
    # from hangman_words import word_list
    # from hangman_art import stages, logo
from replit import clear

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Prevent repeated guesses (line 41)
guessed_letters = []

#####################################################
while not end_of_game:
    guess = input("Guess a letter: ").lower() 
    
    # To clear and clean up the UI
    clear()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Prevent repeated guesses
    guessed_letters += guess
    if guessed_letters.count(guess) > 1:
        print(f"You guessed {guess}. You have already guessed this letter.")
    #Check if user is wrong.
    elif guess not in chosen_word:        
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
