def add(num1,num2):
    return f"The sum of {num1} and {num2}: {int(num1) + int(num2)}"

def subtract(num1,num2):
    return f"The diffirence of {num1} and {num2}: {int(num1) - int(num2)}"

def multiply(num1,num2):
    return f"The product of {num1} and {num2}: {int(num1) * int(num2)}"

def divide(num1,num2):
    return f"The quotient of {num1} and {num2}: {int(num1) / int(num2)}"

def power(num1,num2):
    return f"The power of {num1} and {num2}: {int(num1) ** int(num2)}"

def exp(num1,num2):
    if int(num2) == 0:
        return "Can not divided by Zero!"
    return f"The remainder of {num1} and {num2}: {int(num1) % int(num2)}"

def calculate(num1,num2,operator):
    while True:
        if operator == '+':
            return add(num1,num2)
        elif operator == '-':
            return subtract(num1,num2)
        elif operator == '*':
            return multiply(num1,num2)
        elif operator == '/':
            if int(num2) == 0:
                return "Can not divided by Zero!"
            return divide(num1,num2)
        elif operator == '**':
            return power(num1,num2)
        elif operator == '%':
            return exp(num1,num2)