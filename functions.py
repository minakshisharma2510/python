def my_function():
    print("hello from a function")
my_function() 


def my_function(name):
    print(name, "hello")
name = input("enter name: ")    
my_function(name)

##calculator
print("---calculator---")
def add(x, y):
    return(x+y)
def subtract(x, y):
    return(x-y)
def multiply(x, y):
    return(x*y)
def divide(x, y):
    return(x/y)
x = eval(input("Enter 1st no.: "))
y = eval(input("Enter 2nd no.: "))
op = input("enter the operation you want to do(+,-,*,/): ")
if op == "+":
    result = add(x,y)
elif op == "-":
    result = subtract(x,y)
elif op == "*":
    result = multiply(x,y)
elif op == "/":
    result = divide(x,y)
else:
    print("invalid input")
print(result)
    
    
##Define a function named 'sum' that takes a list of numbers as input
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
user_input = eval(input("enter a list of no.s seprated by (,): "))
print(sum(user_input))


##Print "odd" or "even" for a given number.
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = eval(input("enter a no.: "))
result = check(num)
print(result)
        
        
##Categorize age group based on user input (child, adult, senior).

def age_group(age):
    if age < 12:
        print("you are a ")
    elif age >= 12 and age < 18 :
        print("you are a teenager")
    elif age >= 18 and age <= 60:
        print("you are an adult")
    elif age > 60:
        print("you are a senior")
    else:
        print("invalid input")
age = int(input("Enter your age in numbers: "))
age_group(age)


## Print the multiplication table of a given number.
def table(num):
    i = 1
    while i < 11:
        result = num*i
        print(f"{num}*{i}={result}")
        i += 1
num = int(input("enter a no.: "))
table(num)
        