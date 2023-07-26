print("Hello My Lord")
print("KNIGHT CALCULATOR hear to serve you")

num1= float(input("Enter your first number:"))
num2= float(input("Enter your second number:"))
op = input("please select your operation(+ , - , * , / , sin , cos , tan , cot , ! , radical ): ")

import math
if op=="+":
    result = num1 + num2
if op=="-":
    result = num1 - num2
if op=="*":
    result = num1 * num2
if op=="/":
    if num2 == 0:
        result= "far as we know, there is no answer, my Lord"
    else:
        result = num1 / num2
if op== "sin":
    result = math.sin(num1)
if op == "cos":
    num1 = int(input("enter your number: "))
    result = math.cos(num1)
 
if op == "tan":
    num1 = int(input("enter your number: "))
    result = math.tan(num1)

if op == "cot":
    num1 = int(input("enter your number: "))
    x = math.tan(num1)

    if x == 0:
        result = "far as we know, there is no answer, my Lord"
    else:
        result = 1 / math.tan(num1)

if op == "!":
    num1 = int(input("enter your number: "))
    result = math.factorial(num1) 

if op == "radical":
   num1 = int(input("enter your number: ")) 
   result = math.sqrt(num1)     

print(result)