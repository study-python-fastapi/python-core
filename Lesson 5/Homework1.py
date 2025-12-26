from operator import add

import calculator
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = str(input("Enter function: "))
if c == "add":
    print(calculator.add(a,b))
elif c == "subtract":
    print(calculator.subtract(a,b))
elif c == "multiply":
    print(calculator.multiply(a,b))
elif c == "divide":
    if b != 0:
        print(calculator.divide(a, b))
    else:
        print("Cant divide by 0")
else:
    print("Please enter a valid input")

