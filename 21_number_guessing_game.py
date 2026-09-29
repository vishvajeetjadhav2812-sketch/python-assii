correct = 50

while True:
    guess = int(input("Enter your guess: "))

    if guess == correct:
        print("Correct Guess!")
        break
    elif guess > correct:
        print("Too High")
    else:
        print("Too Low")
