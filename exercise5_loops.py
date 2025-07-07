''' ===Loops (for, while) :- '''

# ## 1 - Print all even numbers from 1 to 100.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end=",")


## 2 - Print the multiplication table of a given number.
# num = int(input("enter a number: "))
# i = 1
# while i < 11:
#     result = num*i
#     print(num,"*", i, "=", result)
#     i+=1


## 3 - Calculate the factorial of a number using a loop.
# num = int(input("Enter a number: "))
# i = 1
# fact = 1
# while i <= num:
#     fact =i*fact
#     i+=1
# print(fact)


## 4 - Write a program to print the Fibonacci series.
# n = int(input("Enter how many terms of Fibonacci series to print: "))
# a = 0
# b = 1 
# i = 0
# while i < n:
#     print(a, end=", ")
#     next_term = a + b
#     a = b
#     b = next_term
#     i += 1


## 5 - Find the sum of digits of a number.

n = int(input("enter the no.: "))
a = [int(i) for i in str(n)]
print(a)
length = 0
sum = 0
while length < len(a):
    sum += a[length]
    length += 1
print("sum of digits: ",sum)



## 6 - Reverse a given string using a loop.

## 7 - Write a program to count the number of vowels in a string.

## 8 - Create a pattern (e.g., triangle of stars) using nested loops.

## 9 - Check whether a number is an Armstrong number.

## 10 - Use a while loop to find the first 10 prime numbers.
