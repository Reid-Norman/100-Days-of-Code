#Imports
from game_data import data
import art
from random import choice
from replit import clear

#Functions 
def item_selector():
    '''A function which chooses a random item from the list and then removes the item from the list to prevent duplicate selections.'''    
    new_item = choice(data)
    data.remove(new_item)
    return new_item
    # I may want to make a duplicate list from which to remove values


def follower_comp(dict_a, dict_b):
    '''A function to compare the number of followers in the 2 inputs and return either 'A or 'B' for the former & latter, respectively.'''
    followers_a = int(dict_a["follower_count"])
    followers_b = int(dict_b["follower_count"])

    if followers_a > followers_b:
        return "A"
    elif followers_a < followers_b:
        return "B"
    else:
        return "SOMETHIN' WHACK"


def point_calc(guess, answer, score):
    '''A function to compare the user_guess to the answer, print the appropritate text, and return an update for the total_score if needed.'''
    if guess == answer:
        clear()
        print(art.logo)
        print(f"You're right! Current score: {score +1}")
        return +1
    else:
        clear()
        print(art.logo)
        print (f"Sorry, that's wrong. Final score: {score}")
        return -(score +1)
    

def print_gui(dict_a, dict_b):
    '''A function to call the appropriate entries from their dict's and print them into f-strings'''
    
    print(f"Compare A: {dict_a['name']}, a {dict_a['description']}, from {dict_a['country']}.")
    print(art.vs)
    print(f"Against B: {dict_b['name']}, a {dict_b['description']}, from {dict_b['country']}.")


##### Start of active code #####

dictionary_b = item_selector()
total_score = 0
print(art.logo)

while total_score >-1:
    #Cycle through the list of options for the game
    dictionary_a = dictionary_b
    dictionary_b = item_selector()
    
    #Function to decide which item has more followers
    result = follower_comp(dictionary_a, dictionary_b)

    #Print fstrings of the items being compared & the vs ASCII Art
    print_gui(dictionary_a, dictionary_b)

    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    #Update the score, compare user_guess & answer, and print appropriate text.
    total_score += point_calc(user_guess, result, total_score)

