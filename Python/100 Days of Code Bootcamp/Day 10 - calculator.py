#Ioannis Apomachos

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

print(logo)

def add(n1 ,n2):
    """This method adds two numbers"""
    return n1+n2

def subtract(n1 ,n2):
    """This method subtracts two numbers"""
    return n1-n2

def multiply(n1 ,n2):
    """This method multiplies two numbers"""
    return n1*n2

def divide(n1 ,n2):
    """This method divides two numbers"""
    return n1/n2

operations_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}



def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations_dictionary:
        print(symbol)
    continue_calculating=True


    while continue_calculating:
        operation_symbol= input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations_dictionary[operation_symbol]
        answer=calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice=input(f"Type 'y' to continue calculating with {answer}, type 'a' to start again or type 'n' to stop ")
        if choice=="y":
            num1=answer
        elif choice=="n":
            continue_calculating=False
            return
        else:
            calculator()

calculator()