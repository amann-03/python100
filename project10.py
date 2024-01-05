# CALCULATOR

import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    
    print(logo)
    num1 = float(input("what's the first number?: "))  # note we have converted to float type and not int so we can have floating pt. numbers as inputs also

    for symbol in operations:
        print(symbol)
    want_continue = True # flag to hold loop

    while want_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what's the second number?: "))
        answer = operations[operation_symbol](num1,num2) # first part gives us the function and second part is the arguments we are passing

        print(f"{num1} {operation_symbol} {num2} = {answer}\n")

        if input(f"type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ")=="y":
            num1 = answer
        else:
            want_continue = False
            os.system('cls')
            calculator()  # recursion
            
calculator() 

# FINISH PROJECT