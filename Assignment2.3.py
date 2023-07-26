print("Hello there")
print("what's up?")
print("let's calculate your GPA")

name = input("enter your First name: ")
family = input("enter your Last name: ")
score1=float(input("Enter your first score:"))
score2=float(input("Enter your second score:"))
score3=float(input("Enter your third score:"))

Avg = (score1+score2+score3)/3
if Avg>=17:
    status="Greate, nice job!"
elif Avg<17 and Avg>=12:
    status="Normal,can be better."
else:
    status="YOU ARE FAIL, Don't worry man, do it next time well :) "
print("Name:",name,"Last name:", family)
print("Average:",Avg, "Status:",status)