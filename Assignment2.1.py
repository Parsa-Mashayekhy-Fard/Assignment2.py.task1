print("Hello My Lord")
print("KNIGHT CALCULATOR here to serve you")

import math

op = input("Please select your operation (+, -, *, /, sin, cos, tan, cot, !, radical): ")
num1 = float(input("Enter your first number: "))
num2 = None

if op not in ["sin", "cos", "tan", "cot", "!"]:
    num2 = float(input("Enter your second number: "))

result = None

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "Far as we know, there is no answer, my Lord."
    else:
        result = num1 / num2
elif op == "sin":
    result = math.sin(math.radians(num1))
elif op == "cos":
    result = math.cos(math.radians(num1))
elif op == "tan":
    result = math.tan(math.radians(num1))
elif op == "cot":
    if math.tan(math.radians(num1)) != 0:
        result = 1 / math.tan(math.radians(num1))
    else:
        result = "Far as we know, there is no answer, my Lord."
elif op == "!":
    result = math.factorial(num1)
elif op == "radical":
    result = math.sqrt(num1)
else:
    result = "Invalid operation, my Lord. Please select a valid one."

print("Result:", result)