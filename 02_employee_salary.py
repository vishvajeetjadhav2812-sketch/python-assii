basic = float(input("Enter basic salary: "))

da = basic * 10 / 100
hra = basic * 20 / 100
gross = basic + da + hra
tax = gross * 5 / 100
net = gross - tax

print("DA =", da)
print("HRA =", hra)
print("Gross Salary =", gross)
print("Tax Deduction =", tax)
print("Net Salary =", net)
