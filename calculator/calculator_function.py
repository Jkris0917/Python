def add(num1,num2):
    return f"The sum of {num1} and {num2}: {num1 + num2}"

def subtract(num1,num2):
    return f"The diffirence of {num1} and {num2}: {num1 - num2}"

def multiply(num1,num2):
    return f"The product of {num1} and {num2}: {num1 * num2}"

def divide(num1,num2):
    if num2 == 0:
        return "Can't divide by zero!"
    return f"The quotient of {num1} and {num2}: {num1 / num2}"

def power(num1,num2):
    return f"The power of {num1} and {num2}: {num1 ** num2}"

def exp(num1,num2):
    if num2 == 0:
        return "Can't divide by zero!"
    return f"The remainder of {num1} and {num2}: {num1 % num2}"

def calculate(num1,num2,operator):

        if operator == '+': return add(num1,num2)
        elif operator == '-': return subtract(num1,num2)
        elif operator == '*': return multiply(num1,num2)
        elif operator == '/': return divide(num1,num2)
        elif operator == '**': return power(num1,num2)
        elif operator == '%': return exp(num1,num2)
