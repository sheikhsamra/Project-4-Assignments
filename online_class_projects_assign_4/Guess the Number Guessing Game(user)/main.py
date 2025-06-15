import random
print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 10)
print("I have secret number between 1 and 10. Can you guess it? ")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too high! Try again: ")
        elif guess < secret_number:
            print("Too low! Try again. ")
        else:
            print("Congratulation! You've guessed the number! ")
            break
    except ValueError:
        print("Invalid input. Please entera number between 1 and 10. ")