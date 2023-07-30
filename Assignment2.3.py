print("Hello there")
print("What's up?")
print("Let's calculate your GPA")

name = input("Enter your First name: ")
family = input("Enter your Last name: ")

# Input validation for scores (0 to 20)
while True:
    try:
        score1 = float(input("Enter your first score (0-20): "))
        score2 = float(input("Enter your second score (0-20): "))
        score3 = float(input("Enter your third score (0-20): "))
        if 0 <= score1 <= 20 and 0 <= score2 <= 20 and 0 <= score3 <= 20:
            break
        else:
            print("Invalid input! Scores must be in the range 0-20.")
    except ValueError:
        print("Invalid input! Please enter a numeric value for the scores.")

avg = (score1 + score2 + score3) / 3
if 20 >= avg >= 17:
    status = "Great, nice job!"
elif 17 > avg >= 12:
    status = "Normal, can be better."
else:
    status = "YOU HAVE FAILED. Don't worry, try again next time :)"

print("Name:", name, "Last name:", family)
print("Average:", avg, "Status:", status)