############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# # The range function goes "up to, but not including". range(1, 20) should be range (1, 21)

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# #If a bug only happens sometimes, try to change your
# # code so it happens all the time. This will reveal at least one of the issues.
# #The error happens when the randint is 6. This is because the computer starts counting at zero. randint(1,6)
# # should be randint(0, 5)

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# # The greater than and lesser than 1994 miss an input of 1994 because nothing is equal to 1994.

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# # The input function takes whatever input it is given and returns it as a string. The age needs to be converted to an
# # integer. An f-string is also needed to make the curly braces work.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #print(pages)
# word_per_page = int(input("Number of words per page: "))
# #print(word_per_page)
# # Printing word_per_page reveals that the output is 0; highlighting that the reassignment of word_per_page is 
# # (==)/ equivalent to   rather than (=)/ equals
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# # Use http://www.pythontutor.com/visualize.html#mode=edit
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# # Following this through the debugger shows that only the last item from the list gets appended because
# # the append functions is not within the for loop.
