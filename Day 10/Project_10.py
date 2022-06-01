import art
import os


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operators = { "+":add, "-":subtract, "/":divide, "*":multiply}
def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    for symbols in operators:
        print(symbols)

    go_again = "y"
    while go_again == "y":
        operation_symbol = input("Choose an operator: ")
        operator_function = operators[operation_symbol]
        num2 = float(input("What's the next number?: "))
        answer = operator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        go_again = input(f"Type 'y' to continue calculating with {answer} or 'n' to start all over: ").lower()
        if go_again == "n":
            os.system("cls")
            calculator()

calculator()

