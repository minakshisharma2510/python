''' ===Variables & Data Types :- '''
## 1 - Create a program that takes a user's name and age and prints a greeting.

user_name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hi ",user_name,"! ", age," suits you well!. Nice to meet you.",sep="")
print(f"Hi {user_name}! {age} suits you well!. Nice to meet you.")



## 2 - Swap two numbers without using a temporary variable.

a = int(input("Enter 1st no.:"))
b = int(input("Enter 2nd no.:"))
print("a =",a,"and b =",b)
a = a + b
b = a - b
a = a - b
print("After swapping a and b. \na =",a,"and b =",b)



## 3 - Given a list of integers, return a list with only unique elements.

list1 = [8,2, 3, 4, 9, 5, 5, 3, 6, 7, 3, 2, 1]
list1 = list(set(list1))
print(list1)



## 4 - Count how many times each character appears in a string.

str1 = input("Type a string or a line or words:\n")
# str1 = "hello world"
user_choice = input("enter the character: ")
str2 = str1.count(user_choice)
print(str2)
 


## 5 - Write a program to convert a tuple into a dictionary.

dict1 = {
    "name" : "Minakshi Sharma",
    "age" : 20,
    "language" : "python"
}
print("dictionary: ",dict1)
tuple_convert = tuple(dict1.items())
print("dictionary to tuple: ",tuple_convert)



## 6 - Create a program to merge two dictionaries.

dict1 = {
    "name" : "Minakshi Sharma",
    "age" : 20,
    "language" : "python",
    # "b" : 8
}
dict2 = {"a" : 1, "b" : 2, "c" : 3}
print(dict1,"\n",dict2)
dict1.update(dict2)
print(dict1)

# merge_dict = dict1|dict2
# merged_dict = {**dict1, **dict2}
# print(merge_dict)



## 7 - Write a program to remove duplicate values from a list using sets.

a = (1, 2, 3, 4, 2, 1, 5, 9, 3, 2, 5)
a = set(a)
print(a)



## 8 - Convert a string to a list of characters and back to a string.

str1 = "hello world"
converted_list = str1.split()
print(converted_list)
str2 = " ".join(converted_list)
print(str2)


## 9 - Find the maximum and minimum values in a list.
numbers = eval(input("Enter a list of number seprated by comma(,): "))
maximum = max(numbers)
minimum = min(numbers)
print("Maximum value in list is ", maximum)
print("Minimum value in list is ", minimum)

## 10 - Write a function to check if a key exists in a dictionary.