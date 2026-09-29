data = float(input("Enter data usage in GB: "))

if data <= 5:
    bill = data * 100
elif data <= 10:
    bill = 5 * 100 + (data - 5) * 150
else:
    bill = 5 * 100 + 5 * 150 + (data - 10) * 250

print("Mobile Data Bill =", bill)
