# guest_name = input("Enter your Name: ")
# print(f"Hi!, {guest_name}.")
# print()
# print("====Welcome to Calculator!====")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# add = num1 + num2
# subtract = num1 - num2
# multiply = num1 * num2
# power = num1 ** num2


# print(f"\nSum of {num1} and {num2} is: {add} ")
# print(f"\nDifference of {num1} and {num2} is: {subtract} ")
# if num2 != 0:
#     print(f"\nQuotient of {num1} and {num2} is: {num1 / num2:.2f} ")
# else:
#     print("Can`t be divided by Zero!")

# print(f"\nProduct of {num1} and {num2} is: {multiply} ")
# print(f"\nPower of {num1} and {num2} is: {power} ")
# if num2 != 0:
#     print(f"\nRemainder of {num1} and {num2} is: {num1 % num2:.2f} ")
# else:
#     print("Can`t be divided by Zero!")

from calculator_function import calculate

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Must be a number!")
            
def main(name):
    print(f"\nHi, {name}")
    print("=== Welcome to Calculator ===")
    
    operators = ['+','-','*','/','**','%',]
    
    while True:
        operator = input("\nChoose Operator ['+','-','*','/','**','%']: ")
        if operator not in operators:
            print("Invalid Operator")
            continue
        
        num1 = get_number("First Number: ")
        num2 = get_number("Second Number: ")
        
        print(calculate(num1,num2,operator))
        
        again = input("\nCalculate again? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break
        
name = input("What is your name?: ")
main(name)
            
