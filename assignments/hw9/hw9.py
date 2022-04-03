"""
Name: Alex Toscano
hw9.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin, Circle, Point


def get_words(file_name):
    in_file = open(file_name, "r")
    return in_file.readlines()


def get_random_word(words):
    word = words[randint(0, len(words)-1)]
    return word.strip('\n')


def letter_in_secret_word(letter, secret_word):
    return letter in secret_word


def already_guessed(letter, guesses):
    return letter in guesses


def make_hidden_secret(secret_word, guesses):
    sec = []
    string = " "
    for letter in secret_word:
        sec.append("_")
    for guess in range(len(guesses)):
        for guess2 in range(len(secret_word)):
            if secret_word[guess2] == guesses[guess]:
                sec[guess2] = guesses[guess]
    return string.join(sec)


def won(guessed):
    for i in guessed:
        if i == "_":
            return False
    return True


def play_graphics(secret_word):
    win = GraphWin("Hangman", 500, 500)


def play_command_line(secret_word):
    attempted = []
    guesses_rem = 6
    while guesses_rem != 0 or won is False:
        print("Already guessed: ", attempted)
        print("Guesses remaining: ", guesses_rem)
        guess = input("guess a letter: ")
        if already_guessed(guess, attempted) is not True:
            attempted.append(guess)
            if letter_in_secret_word(guess, secret_word) is not True:
                guesses_rem = guesses_rem - 1
    if guesses_rem == 0:
        print("sorry, you did not guess the word." + "\n"
              + " the secret word was ", secret_word)
    else:
        print("winner!")




if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
