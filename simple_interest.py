principal = eval(input("Enter the amount you invested: "))
rate = eval(input("Enter the rate of interest per year: "))
time = eval(input("Enter the time in years: "))
si = (principal * rate * time) / 100
print("simple interest is ", si)