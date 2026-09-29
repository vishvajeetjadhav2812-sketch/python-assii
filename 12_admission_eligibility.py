maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 3

if maths >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
