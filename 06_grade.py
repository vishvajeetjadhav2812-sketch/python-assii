percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage")
elif percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")
