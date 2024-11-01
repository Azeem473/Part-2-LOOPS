import random
correct_number = random.randint(1,50)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1  
    if guess < correct_number:
        print("Too low! Try again.")
    elif guess > correct_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number {correct_number} in {attempts} attempts.")
        break
    print("Please enter a valid integer.")
    continue