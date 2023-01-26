import random
from words import words
from time import sleep
import os
import colorama

from colorama import Fore, Style

from graffiti import welcome


colorama.init(autoreset=True)


def display_hangman(lives):
    hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return hangman[lives]

    """
    Greeting function with logo  and welcome the player to begin the game
    """
    print(Fore.GREEN + welcome)
    sleep(1)


def game_start():

    """
    Instructions for game 
    """
    print("Welcome Dear Friend! It is time for game.\n")
    name = input(f"{Fore.RED+Style.BRIGHT}What is your name?\n")

    print(f"{Fore.YELLOW+Style.BRIGHT}Hello" + " " + name,)
    print("--------------------------------------")
    print("Please read the following instructions\n"
          "to find your way to and trough the game.\n")
    print(
        "1.You have to guess the secret word one letter at a time \n"
        "before you are out of lives.\n"
      )
    print(
        "2.After each incorrectly answered \n"
        "letter your Hangman will start to  build.\n"
      )
    print(f"3. {Fore.RED+Style.BRIGHT}You have only 7 tries")
    print()
    print(
        "When you reach 0 lives. You will be Hanged!\n"
        "Don't worry you can restart the game!"
      )
    print("Good luck ! " + name)
    print()
    print("============================")
    print(f"{Fore.BLUE+Style.BRIGHT}Try to guess the Word")
    print()


def get_random_word():
    """
    Get random words
    """
    word = random.choice(words)
    print(word)
    return word.upper()
    word_completion = "_" * len(word) 
    print(word_completion)


def hangman_play():
    """
    Display output for each word, guess rigth letter
    """

    word = get_random_word()
    guessed = False
    correct_letters = []
    guessed_wrong = []
    lives = 7
    game_won = False
    hangman_won = False
    while not game_won and lives > 0:
    word = '_'
    for letter in word:
    if letter in correct_letters:
    word += letter
    else:
    word = ''
    print("The word is:", word, "\n")
    if "_" not in word:
    game_won = True
    hangman_won = True

# geussing letters in a secred word, all guess full word and win
    guess = input("Please enter a letter or word:").upper()
    if len(guess) == 1 and guess.isalpha():
    if guess in correct_letters or guess in guessed_wrong:
    print(f"{Fore.RED+Style.BRIGHT}You already guessed the letter", guess)

    elif guess not in word:
    print(guess, f"{Fore.RED+Style.BRIGHT}is not in the word")
    guessed_wrong.append(guess)
    lives -= 1
    print(display_hangman(lives))
  
    else:
    print(f"{Fore.GREEN+Style.BRIGHT}Good job!",guess,"is in the word!")
    correct_letters.append(guess)
    elif len(guess) == len(word) and guess.isalpha(): 
    if guess == word:
    print(f"{Fore.GREEN+Style.BRIGHT}Congrs you guess the word you win ")
    correct_letters.append(guess)
    game_won = True
    hangman_won =True
    else: 
    print("Incorrect guess")
    guessed_wrong.append(guess)
    lives -= 1 
    print(display_hangman(lives))

    
def hangman_end():
    """
    Function to start game from beggining
    """

    play_again = input("Do you want start game again?")
  
    print("Please enter 'Y' OR 'N'")

    if play_again == "Y":
    print("Let's satrt again")
    elif play_again == "N":

    print("Thanks for play,see you next time")


def main():
    """
    Function to return a game from beginning
    """
    game_start()
    hangman_play()

    main()