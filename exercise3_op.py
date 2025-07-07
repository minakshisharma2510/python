''' ===Operators (Arithmetic, Logical, Comparison, Assignment) :- '''

## 1 - Write a calculator program that performs addition, subtraction, multiplication, division, and modulo.

print("*calculator*")
num1 = eval(input("Enter 1st no.:"))
num2 = eval(input("Enter 2nd no.:"))
op = input("Enter the operator sign(+,-,*,/,%): ")
if  op == "+":
    print(num1, "+", num2, "is")
    num1 = num1 + num2
    print(num1)   
elif op == "-":
    num1 = num1 - num2
    print(num1)
elif op == "*":
    num1 = num1 * num2
    print(num1)
elif op == "/":
    num1 = num1 / num2
    print(num1)
elif op == "%":
    num1 = num1 % num2
    print(num1)
else:
    print("invalid operator")



## 2 - Check if a number is divisible by both 3 and 5.

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5")
else :
    print(num, "is not divisible by both 3 and 5")



## 3 - Compare two numbers and print the larger one.

num1 = input("Enter 1st no.: ")
num2 = input("Enter 2nd no.: ")
print(type(num1))
print(type(num2))
if num1 < num2 :
    print(num2, "is larger no.")
elif num1 > num2 :
    print(num1, "is larger no.")
elif num1 == num2: 
    print(num1, "=", num2)
else:
    print("invalid input")



## 4 - Check if a given number is even and greater than 100.

num = eval(input("Enter a number: "))
if num % 2 == 0 and num > 100:
    print(num, "is an even no. and greater than 100")
elif num % 2 == 0 and num <= 100:
    print(num, "is an even no. but not greater than 100")
elif num % 2 != 0 and num > 100:
    print(num, "is not an even no. but greater than 100")
else:
    print(num,"is neither an even no. and nor greater than 100")
    
    

## 5 - Use logical operators to verify if a student passed (marks > 33 and attendance > 75%).

marks = int(input("enter your marks: "))
attendance = int(input("enter your attendance in % : "))
if marks > 33 and attendance > 75:
    print("you are passed ")

else: 
    print("failed")


## 6 - Use compound assignment operators (+=, -=) to update a score variable.

score = 50  
score += 10 
print("After adding 10, score =", score)
score -= 5  
print("After subtracting 5, score =", score)



## 7 - Write a program to swap values using arithmetic operators only.

a = int(input("Enter 1st no.:"))
b = int(input("Enter 2nd no.:"))
print("a =",a,"and b =",b)
a = a + b
b = a - b
a = a - b
print("After swapping a and b. \na =",a,"and b =",b)


## 8 - Demonstrate short-circuiting with logical operators.

x = int(input("enter a no.: "))
if x < 2 or x > 5:
    print("True")

    
    

## 9 - Check if two strings are equal using comparison operators.

str1 = input("Type a 1st string:\n")
str2 = input("Type a 2nd string:\n")
if str1 == str2:
    print("strings are same")
else:
    print("not same")


## 10 -Implement a simple grade calculator using assignment and comparison operators.

a = eval(input("enter 1st no.: "))
b = eval(input("enter 2nd no.: "))
operator = input("enter operator sign that you want to do (+,-,*,/): ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("invalid input")