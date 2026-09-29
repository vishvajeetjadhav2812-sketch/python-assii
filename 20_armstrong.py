num = int(input("Enter number: "))

original = num
count = 0
temp = num

while temp > 0:
    count = count + 1
    temp = temp // 10

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
