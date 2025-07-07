print("*calculator*")
repeat = "Y"
while repeat == "Y" or repeat == "y":
    num1 = eval(input("Enter 1st no.:"))
    num2 = eval(input("Enter 2nd no.:"))
    op = input("Enter the operator sign(+,-,*,/): ")
    if  op == "+":
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
    else:
        print("invalid operator")

    repeat = input("Do you want to continue or not (Y/N):")
if repeat=="Y" or repeat =="y":
    print("continue")
else:
    print("exiting...")
