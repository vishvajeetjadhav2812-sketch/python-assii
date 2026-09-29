num = int(input("Enter number: "))

count = 0
largest = 0
smallest = 9

while num > 0:
    digit = num % 10
    count = count + 1

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Number of digits =", count)
print("Largest digit =", largest)
print("Smallest digit =", smallest)
