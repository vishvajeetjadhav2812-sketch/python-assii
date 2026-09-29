start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count_prime = 0

for num in range(start, end + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)
        count_prime = count_prime + 1

print("Total Prime Numbers =", count_prime)
