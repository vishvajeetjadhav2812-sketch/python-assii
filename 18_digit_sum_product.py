num = int(input("Enter number: "))

sum = 0
product = 1

while num > 0:
    digit = num % 10
    sum = sum + digit
    product = product * digit
    num = num // 10

print("Sum =", sum)
print("Product =", product)
