#Explain the concept of string immutability in Python.
my_string = "hello"
print(my_string) # Prints the memory address of the string object
print(id(my_string))
print(id(my_string))

my_string = my_string + " world" # This creates a *new* string object
print(my_string) # Prints a different memory address, as it's a new object
print(id(my_string))