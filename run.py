import random
from words import WORDS
import os
import colorama

from colorama import Fore, Style

from graffiti import welcome

colorama.init(autoreset=True)

def display_hangman(tries):
   hangman = [
    '''
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
========='''
  ]

# Alionareturn stage[tries]


def hangman_welcome():


    
    """
 Greeting function with logo  and rules to player to begin the game

   """


print(Fore.GREEN + welcome)


def game_start():
  """
Create the rules for game and function to start the game
  """


print("Welcome Dear Friend! It is time for game.\n")
name = input(f"{Fore.RED+Style.BRIGHT}What is your name?\n")
print("Hello" + " " + name)
print("Please read the following instructions\n"
      "to find your way to and trough th game.\n")
print(
  "1.You have to guess the secret word one letter at a time\n before you are out of lives.\n"
)
print(
  "2.After each incorrectly answered letter your Hangman will start to  build.\n"
)
print("3. You have 6 tries")
print(
  "When you reach 0 lives. You will be Hanged!\n Don't worry you can restart the game!"
)
print("Good luck ! " + name)


def getRandomWords():
    word = random.choice(WORDS)
    print(WORDS)
    return word.upper()


def game_play():
    word_lenght = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Lets play Hangman !")
