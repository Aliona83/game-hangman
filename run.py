import random, words
from time import sleep
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
  "1.You have to guess the secret word one letter at a time\n before you are out of lives.\n"
)
print(
  "2.After each incorrectly answered letter your Hangman will start to  build.\n"
)
print(f"3. {Fore.RED+Style.BRIGHT}You have only 6 tries")
print(
  "When you reach 0 lives. You will be Hanged!\n Don't worry you can restart the game!"
)
print("Good luck ! " + name)
print()
print("============================")
print(f"{Fore.BLUE+Style.BRIGHT}Try to guess the Word")


  
word = random.choice(words.WORDS).lower()
word = word.lower()
output = list(len(word)*'_')
lives = 6
gameWon = False


def print_hangman():


 def check_letters(letters,word):
  """
  Function cheack the right and wrong letters in a word
  """
  global output
  for i in range(0,len(word)):
    print("_",end=" ")
    letter = word[i]
    if guess == letter:
      output[i] = guess
      if'__' not in output:
        return True
        print("Well done")
      else:
          return False
      
while gameWon == False and lives > 0:
  guess =input("Guess a letter or an entire word:").lower()
  if len(guess) != 1:
    print("Please enter a single letter")
  elif not guess.isalpha():
      print("Please enter a letter")
  else:
      #  return guess
    guess = guess.lower()
  

  if guess == word:
    gameWon = True
  else:
    lives -= 1

if gameWon:
  print("Well done you are win")
else:
    print("YOU FAILED the word was:",word)
  
def play_again():
  """
  Ask the user play again
   """
  answer = input("Do you want to play again(y/n)").lower()
  if answer == "y":
    return True
  elif answer == "n":
      return False
  else:
        print("Please enter y or n")

