def isnumeric(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def add(n1, n2):
    validate_input(n1, n2)
    return float(n1) + float(n2)

def subtract(n1, n2):
    validate_input(n1, n2)
    return float(n1) - float(n2)

def multiply(n1, n2):
    validate_input(n1, n2)
    return float(n1) * float(n2)

def divide(n1, n2):
    validate_input(n1, n2)
    if n2 == 0:
        print("You can't divide by zero.")
        exit()
    else:
        return float(n1) / float(n2)

def validate_input(num1, num2):
    if num1.isnumeric() == False or num2.isnumeric() == False:
        print("Invalid input. Please enter a number.")
        exit()        
    else:
        return num1, num2

def validate_operation(operation):
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please enter a valid operation.")
        return False
    else:
        return operation

operations = {
'+': add, 
'-': subtract,
'*': multiply,
'/': divide,
}

def calculator():
    print("\t\tMath Calculator")

    num1 = input("What is the first number?: ")
    run = True
    while run: 
        for e in operations:
            print(e)
        operation = input("Type a math operation: ") 
        operation = validate_operation(operation)
        num2 = input("What is the next number?: ")
        num1, num2 = validate_input(num1, num2)
    
        calculation = operations[operation]
        answer = calculation(num1, num2)
    
        print(f"{num1} {operation} {num2} = {answer}")
        print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")
        continue_calc = input("Type y/n/new: ")
        if continue_calc == 'y':
            run = True
            num1 = answer
        elif continue_calc == 'n':
            run = False
            print("\nTurning off.")
            exit()
        elif continue_calc == 'new':
            calculator()
        else:
            print("Invalid response.")
            run = False
            print("\nTurning off.")
calculator()