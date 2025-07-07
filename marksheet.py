name = input("Enter your name:")
standard = input("Enter your class:")
english = eval(input("Enter your marks in English: "))
maths = eval(input("Enter your marks in Maths: "))
science = eval(input("Enter your marks in Science: "))
total = english + maths + science
percentage = (total / 300) * 100
print("Name: ", name)
print("Class: ", standard)
print("Total marks obtained: ", total)
print("Percentage: ", percentage)
