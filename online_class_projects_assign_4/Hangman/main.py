import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ________|""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ________|""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ________|""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ________|""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ________|""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        ________|""",
        """
           -----
           |   |
               |
               |
               |
               |
        ________|"""
    ]
    return stages[tries]

def design_hangman():
    print("🎨 Welcome to HANGMAN: Design Edition!\n")
    words = ["python", "javascript", "branding", "photoshop", "logo", "typography"]
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    input("Press Enter to start the game...")

    while tries >= 0:
        clear_screen()

        print(print_hangman(tries))

        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display.strip())

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You did it, Design! The word was:", word.upper())
            break

        guess = input("\n🎯 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Only single letters allowed!")
            input("Press Enter to try again...")
            continue

        if guess in guessed_letters:
            print("🔁 Already guessed that letter.")
        elif guess in word:
            print(f"✅ Nice! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"❌ Nope! '{guess}' is not in the word.")
            guessed_letters.append(guess)
            tries -= 1

        if tries < 0:
            clear_screen()
            print(print_hangman(0))
            print("\n💀 Oh no! The final design failed.")
            print("The word was:", word.upper())
            break

    print("\n🖋️ Game Designed by: Samra Moinuddin — The Creative Coder 👑")

# Start the game
if __name__ == "__main__":
    design_hangman()
