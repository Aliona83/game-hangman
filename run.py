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


def getRandomWords(WORDS):
  """
  Randomly chooses words from the list
  """

  word = random.choice(WORDS).lower()


  guessed_right = []
  guessed_wrong =[]
  tries = 6
  hangman_count = -1
  while tries > 0:
       output = ''
       for letter in word:
        if letter in guessed_right:
         output += letter
       else:
         output  += '_'
       if output == word:s
       break

       print("Guess the word: ",output)
       
      print(tries, " chances left")


   
 
   


# def game_play(WORDS):
#     word_lenght = "_" * len(word)
#     guessed = False
#     guessedLetters = []
#     guessedWords = []
#     tries = 6
#     print("Lets play Hangman !")

#     while not guessed and tries > 0:
#     guess = input(f"{Fore.GREEN+Style.BRIGHT}Please guess a letter or word:")
#     if(guess) == 1 and guess.isalpha():
#         if guess in guessedLetters:
#            print("You already guessed the letter", guess)
#         elif guess not in word:
#            print(guess, f"{Fore.RED+Style.BRIGHT}is not in the word.")
#         elif len(guess) == len(WORDS)

#         tries -= 1

