def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number: "))

    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick the operation to solve the problem: ")
        num3 = int(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num3)

        print(f"{num1} {operation_symbol} {num3} = {answer}")

        if input("Type y to continue calculation and type no to exit: ") == "y":
            calculator()
        else:
            should_continue = False
calculator()