from operator import truediv


def add(n1, n2):
    return n1 + n2
# TODO: Write our the other 3 functions - subtract, multiple and divide.
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# TODO: Add these functions into a dictionary as the values. Keys = "+","-","*","/"
calculator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#TODO: Use the dictionary operations to perform the calculations. Multiple 4 * 8 using the dictionary.
#print(calculator_functions["*"](4,8))
import art

def calculator():
    print(art.logo)
    should_accumulate = True
    n1 = float(input("What is the first number?: "))

    while should_accumulate:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What is the next number?: "))
        result = calculator_functions[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' "
                                     f"to start a new calculation: ")



        if continue_calculating == "y":
            n1 = result
        else:
            print("\n" * 20)
            should_accumulate = False
            calculator()

calculator()
