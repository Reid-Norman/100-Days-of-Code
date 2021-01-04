
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
}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))  
    for symbol in operations:
        print(symbol)
    calculation_complete = True
    
    while calculation_complete:
        operation_symbol = input("Pick an operation from the stated options: ")
        num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: \n")
        if to_continue == "y":
            num1 = first_answer           
        else:
            calculation_complete = False
            replit.clear()
            calculator()
            #Using Recursion: Calling the calc. function within the calc. function. Effectively restarting it.
###############################################################

calculator()
