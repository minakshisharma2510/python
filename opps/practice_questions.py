'''## Create Person as a base class and student as derived class
 Student has id and name as parameter, and student has course and grade,
  call all the details of students.'''

# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def data(self):
#         print(f"Name: {self.name}\nID:{self.id}")

# class Student(Person):
#     def __init__(self,name,id,course,grade):
#         super().__init__(name,id)
#         self.course=course
#         self.grade=grade
#     def det(self):
#         print(f"course:{self.course}\ngrade:{self.grade}")
# info=Student("shubham",709,"ai with python",7.04)
# info.data()
# info.det()


"""Design a class Product with attributes name, price.
Create a class DiscountedProduct that inherits from Product and adds a method to calculate price after discount.
Tasks:
Accept a discount percentage as input.
Calculate and return the final price after discount.
Print a bill showing original and discounted price."""

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
    
# class Discount(Product):
#     def __init__(self,name,price):
#         super().__init__(name,price)
#     user=int(input("enter the discount(%): "))
#     def discount(self):
#         after_dis=self.user/100*self.price
#         total=self.price-after_dis
#         print(f"Bill--------> \nproduct={self.name} \nprice:{self.price} \ndiscount:{self.user}% \nTotal-{total}rs")
# a=input("enter the product: ")
# b=int(input("enter the price: "))
# call=Discount(a,b)
# call.discount()



''' ## animal question'''
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(Self):
#         print("make a sound")    
        
# class Dog(Animal):
#     def __init__(self,name):
#         super().__init__(name)
        
#     def speak(self):
#         print("bark")
        
# buddy = Dog("buddy")
# buddy.speak()


'''calculation'''
# base addition 
# method calculator                       
# drived substraction
# class Addition:
#     def __init__(self, num1, num2):
#         self.n1 = num1
#         self.n2 = num2 
        
#     def calculate(self):
#         print("addition is ", self.n1 + self.n2)
        
# class Subtraction(Addition):
#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)
        
#     def calculate(self):
#         print("subtraction is", self.n1 - self.n2)
        
# num = Subtraction(1,3)
# num.calculate()

# num = Addition(3,5)
# num.calculate()


'''### multilevel Inheritance'''
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(Self):
#         print("make a sound")    
        
# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
        
#     def speak(self):
#         print("bark")
        
# class Cat(Dog):
#     def __init__(self, name, age , breed):
#         super().__init__(name,age)
#         self.breed = breed
        
#     def speak(self):
#         print("cat meaow")

# name = input("enter the name of animal: ")
# age = input(f"enter the age of {name}:")
# breed = input("enter the breed of "  + name + ":")

# cat = Cat(name, age, breed)
# cat.speak()


'''Create Person as a base class and student as derived class, 
Student has id and name as parameter, and student has course and grade, 
call all the details of students.'''

# class Person:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#     def data(self):
#         print(f"Name = {self.name}\nId = {self.id}")
        
# class Student(Person):
#     def __init__(self,id, name, course, grade):
#         super().__init__(id,name)
#         self.course = course
#         self.grade = grade
#     def data(self):
#         print(f"course = {self.course} \ngrade = {self.grade}")

# student_info = Student(705, "minakshi", "python", "A")
# Person.data(student_info)
# student_info.data()



"""Design a class Product with attributes name, price.
Create a class DiscountedProduct that inherits from Product and adds a method to calculate price after discount.
Tasks:
Accept a discount percentage as input.
Calculate and return the final price after discount.
Print a bill showing original and discounted price."""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def details(self):
        print(f"product name: {self.name}\n product price: {self.price}")
        
class DiscountProduct(Product):
    def __init__(self, name, price, discount,):
        super().__init__(name, price)
        self.discount = discount
        self.discounted_price = (self.price - ((self.discount / 100) * self.price))
    def final_price(self,):
        print(" price after the discount is:  ", (self.discount/100) * self.price)
        print("---bill---")
        print(f"Product Name: {self.name}")
        print(f"actual price: {self.price}")
        print(f"Discount: {self.discount}%")
        print(f"discounted price: {self.discounted_price}")
name = input("enter the name of the product: ")     
price = int(input("enter the actual price of product:"))
discount = int(input("enter the dicount you want to give on product in %: "))
  
bill = DiscountProduct(name, price, discount,)
bill.final_price()


