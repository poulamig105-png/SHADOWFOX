# Intermediate Task 2: Hangman
# A simple word-guessing game with hints and visual progress.

import random

words = {
    "python": "A popular programming language.",
    "computer": "An electronic machine used to process data.",
    "database": "An organized collection of data.",
    "algorithm": "A step-by-step procedure for solving a problem.",
    "developer": "A person who creates software."
}

word = random.choice(list(words.keys()))
hint = words[word]

guessed = set()
wrong_guesses = 0
max_wrong = 6

stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =======
    """
]

print("=== HANGMAN ===")
print("Hint:", hint)

while wrong_guesses < max_wrong:
    display = " ".join(letter if letter in guessed else "_" for letter in word)
    print(stages[wrong_guesses])
    print("Word:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    if all(letter in guessed for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter (or type 'hint'): ").lower().strip()

    if guess == "hint":
        print("Hint:", hint)
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.add(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(stages[wrong_guesses])
    print("Game over! The word was:", word)
