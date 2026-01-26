
# Number Guessing Game 🎯
# Beginner-friendly Python project

import random

def play_game():
    secret = random.randint(1, 10)
    attempts = 3

    print("🎯 Guess the number between 1 and 10")
    print(f"You have {attempts} attempts")

    while attempts > 0:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("❌ Please enter a number")
            continue

        guess = int(guess)

        if guess == secret:
            print("🎉 Congratulations! You guessed it right.")
            return
        elif guess < secret:
            print("📉 Too low!")
        else:
            print("📈 Too Yes high!")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"😢 Game over! The number was {secret}")

if __name__ == "__main__":
    play_game()
