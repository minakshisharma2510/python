''' ===Conditional Statements (if, elif, else) :- '''

## 1 - Write a program to check if a number is positive, negative, or zero.

x = eval(input("enter a no.: "))
if x == 0:
    print("its zero")
elif x % 2 != 0:
    print(x,"is a negative no.")
else:
    print(x, "is a positive no.")
    

## 2 - Create a simple login system using if-else.

user1 = {"user_name" : "minakshi", "password" : "minakshi123"}
user2 = {"user_name" : "sharma", "password" : 1234 }
# user1 = "minakshi"
# password1 = "minakshi123"
# user2 = "sharma"
# password2 = 1234
print("----Login Page----")

user_name = input("User Name : ")
password = input("password : ")
    
if user_name == user1["user_name"] and password == user1["password"]:
    print("Login successful - Welcome Minakshi!")
elif user_name == user2["user_name"] and password == user2["password"]:
    print("Login successful - Welcome Sharma!")
else:
    print("Invalid username or password")
 
    
      
## 3 - Write a program to find the largest of three numbers.

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest no.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest no.")
else:
    print(num3, "is the largest no.")


## 4 - Check if a year is a leap year.

year = int(input("Enter a year: "))
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


## 5 - Write a temperature converter with options for Celsius <-> Fahrenheit.
temp = float(input("Enter the temperatur value that you want to convert:"))
unit = input("In which unit you want to convert the temperature(C/F)").upper()
if unit=="C":
    c = (5/9 *(temp-32))
    print(c)
elif unit == "F":
    f = ((9/5 *temp)+32)
    print(f)
else:
    print("unit is invalid")
    

## 6 - Print "odd" or "even" for a given number.

num = int(input("enter any number:"))
if num%2 !=0:
    print("Wierd")
elif num%2==0:
    print("not wierd")
elif num%2 == 0 and 0<num<=50:
    print("not wierd")
elif num%2==0 and num>50:
    print ("wierd")


## 7 - Categorize age group based on user input (child, adult, senior).
age = int(input("Enter your age in numbers: "))
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



## 8 - Check if a character is a vowel or consonant.
letter = input("Enter a letter in a-z:")#.lower()
if letter in ( "A","a", "E","e", "I", "i", "O","o","U","u"):
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")



## - Check whether a number is prime using conditional statements.

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
else:
    print("Not a prime number")
