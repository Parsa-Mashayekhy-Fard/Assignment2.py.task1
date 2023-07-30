a = float(input("Enter your first side: "))
b = float(input("Enter your second side: "))
c = float(input("Enter your third side: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print("These numbers can form a triangle.")
    else:
        print("These numbers can't form a triangle.")
else:
    print("Invalid side lengths. All sides must be greater than zero to form a triangle.")