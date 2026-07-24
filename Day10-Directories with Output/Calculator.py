def add (n1,n2):
    return n1+n2

def subtract (n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2


operations={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    should_calculate = True
    num1= float(input('What is the first number:\t'))
    while should_calculate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Select and operation')
        num2= float(input('What is the second number:\t'))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(f'type y if you want to continue calculating with {answer} or type n to start a new calculation ').upper()

        if choice== "Y":
            num1=answer
        else:
            should_calculate=False
            calculator()

calculator()

