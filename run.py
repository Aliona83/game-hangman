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
reveal = list(len(word)*'_')
print(reveal)
lives = 6
gameWon = False

# Pick a word

guessed_right = []
guessed_wrong =[]
hangman_count = -1
  
word = ''
while lives > 0:
       output = ''
       for letter in word:
        if letter in guessed_right:
         output += letter
       else:
         output  += '_'  # Dash for each letter in a word
       if output == word:
        break

       print("Guess the word: ",output)
       print(lives," lives left")
       guess = input().lower()
       if guess in guessed_right or guess in guessed_wrong:
         print("Already guessed", guess)
       elif guess in word:
          print(f"{Fore.GREEN+Style.BRIGHT}Awesome job! You guessed a correct letter!")
       else:
            print(f"{Fore.RED+Style.BRIGHT}Sorry! You have guessed a wrong letter!")
            hangman_count = hangman_count + 1
            tries = lives - 1 
            guessed_wrong.append(guess)


       if lives > 0:
        print("You guessed th word and you win!!!")
       else:
        print("Sorry you guessed the wrong letter.Try again.")


   
 
   

