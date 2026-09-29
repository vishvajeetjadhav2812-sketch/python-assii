while True:
    print("\n--- MENU ---")
    print("1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number: "))
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print("Prime Number")
        else:
            print("Not Prime")

    elif choice == 2:
        num = int(input("Enter number: "))
        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif choice == 3:
        num = int(input("Enter number: "))
        original = num
        sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** 3
            temp = temp // 10

        if sum == original:
            print("Armstrong Number")
        else:
            print("Not Armstrong")

    elif choice == 4:
        num = int(input("Enter number: "))
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        print("Factorial =", fact)

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
