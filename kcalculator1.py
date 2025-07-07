print("Calculator")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
     return x / y
user_input = input("Enter your choice (add/subtract/multiply/divide): ").lower()
x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))
 
if user_input == "add":
    print(f"The result of addition is: {add(x, y)}")
elif user_input == "subtract":
    print(f"The result of subtraction is: {subtract(x, y)}")
elif user_input == "multiply":
    print(f"The result of multiplication is: {multiply(x, y)}")          
elif user_input == "divide":
    print(f"The result of division is: {divide(x, y)}")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
    
