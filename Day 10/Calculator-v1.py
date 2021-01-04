
#Calculator

import replit
import art

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2 
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide

calculation_complete = True

while calculation_complete == True:
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    choice = input("Pick an operation from the stated options: ")
    num2 = int(input("What's the second number?: "))


    calculation_function = operations[choice]
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {choice} {num2} = {first_answer}")

    to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: \n")
    if to_continue == "y":
        calculation_complete = False
        
    else:
        calculation_complete = True
########################################################

    while calculation_complete == False:
        choice = input("Pick another operation from the previous options: ")
        num3 = int(input("What's the next number?: "))
        calculation_function = operations[choice]
        #The continuation of answer is the important reason to use return over print in this assignment
        second_answer = calculation_function(first_answer, num3)
        print(f"{first_answer} {choice} {num3} = {second_answer}")
        
        # Update the calc. 
        first_answer = second_answer
        
        to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: \n")
        if to_continue == "y":
            calculation_complete = False
            
        else:
            calculation_complete = True
            replit.clear()
