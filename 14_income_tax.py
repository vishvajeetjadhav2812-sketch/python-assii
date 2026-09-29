income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 5 / 100
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 20 / 100
else:
    tax = 112500 + (income - 1000000) * 30 / 100

print("Tax Payable =", tax)
