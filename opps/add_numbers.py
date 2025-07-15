class Numbers:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("addition of two numbers is: ",self.num1+self.num2)
class AddNumbers(Numbers):
    def __init__(self, a, b,c):
        super().__init__(a, b,)
        self.num3=c

    def add1(self):
        print("addition of three numbers is:",self.num1+self.num2+self.num3)   

user_num1=int(input("Enter a number(a): "))
user_num2=int(input("Enter another number(b): "))
user_num3=int(input("Enter 3rd number(c): "))

p1=AddNumbers(user_num1,user_num2,user_num3)
p1.add()
p1.add1()