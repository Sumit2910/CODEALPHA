import random
import nltk
from nltk.corpus import words

nltk.download('words')

word_list = words.words()

def choose_word():
    return random.choice(word_list).lower()

def display_word(word, correct_guesses):
    return ''.join([letter if letter in correct_guesses else '_' for letter in word])

def play_hangman():
    word = choose_word()
    correct_guesses = []
    incorrect_guesses = []
    max_attempts = 6

    print("Welcome to Hangman!")

    while len(incorrect_guesses) < max_attempts:
        current_word = display_word(word, correct_guesses)
        print("\nCurrent word: ", current_word)
        print("Incorrect guesses: ", ' '.join(incorrect_guesses))
        guess = input("Guess a letter: ").lower()

        if guess in correct_guesses or guess in incorrect_guesses:
            print(f"You already guessed '{guess}'. Try again!")
        elif guess in word:
            correct_guesses.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            print(f"Sorry, '{guess}' is not in the word.")
        
        if all(letter in correct_guesses for letter in word):
            print(f"\nCongratulations! You guessed the word '{word}'!")
            break
    else:
        print(f"\nGame Over! The word was '{word}'.")

play_hangman()
