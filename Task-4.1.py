import random

words = ["Beautiful", "Selenium", "Compiler", "Random", "Interpreter", "Execution", "Programming"]

word = random.choice(words).lower()  

print("User has to guess the word")
max_attempts = 5  
print(f"No. of wrong attempts allowed: {max_attempts}")
print("Let's start!")

guessed_word = ["_"] * len(word)  
wrong_attempts = 0

while wrong_attempts < max_attempts:
    print(" ".join(guessed_word))  

    letter = input("Enter a letter: ").lower()  

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue

    if letter in word:
        print(f"Yes, the letter '{letter}' is correct!")
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        if "".join(guessed_word) == word:
            print(f"Congratulations! You guessed the word: '{word}'")
            break
    else:
        print(f"Letter '{letter}' is not in the word.")
        wrong_attempts += 1

if wrong_attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The word was '{word}'.")
