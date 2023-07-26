a = float(input("enter your first side: "))
b = float(input("enter your second  side:"))
c = float(input("enter your third side: "))

if a+b>c and a+c>b and b+c>a and a!=0 and b!=0 and c!=0 :
    print("These number can form a triangle")
else:
    print("These number can't form a triangle") 