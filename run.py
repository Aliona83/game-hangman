import random, words
from time import sleep
import os
import colorama

from colorama import Fore, Style

from graffiti import welcome

colorama.init(autoreset=True)
# def display_hangman(lives):
#  hangman = [
#     '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# ========='''
#   ]
#  return stage[lives]

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


# game_start()


def get_random_word():
  """
  Get random words
  
  """
  word = random.choice(words.WORDS)
  return word.upper()
  print(get_random_word())


def hangman_play():
  """
  
  """
  output = "_"*len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  lives = 6
  print("Let's start the game!")
  print(display_hangman(lives))
  print("\n")

  word = get_random_word()

  while not guessed and lives > 0:
    guess = input("Please enter a letter or word").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guessed the letter",guess)

      elif guess not in word:
        print(guess,"is not in the word")
        lives -=1
        guessed_letters.append(guess)
      else:
        print("Good job!",guess,"is in the word!")
        guessed_letters.append(guess)
        word_list = list(output)
        position_letter = [i for i,letter in enumerate(word) if letter == guess]

        for index in position_letter:
          word_list[index] = guess
          output =" ".join(word_list)
          
       
          if "_" not in output:
            guessed = True
          elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
              print("You already guessed the letter", guess)
          elif guess != word:
              print(guess,"is not the word")
          lives -=1
          guessed_letters.append(guess)
        
        else:
              guessed = True
              output = word
    else:
              print:("Not a valid guess")
              print(display_hangman(lives))
              print(output)
              print("\n")
              if guessed:
                print("Congrs you guess the word you win ")
              else:
                print("Sorry you lost.")




def main():
  """
  Function to return a game from beginning
  """
  game_start()
  word = get_random_word()

  while input("Play again?(N/Y").upper()=="Y":
    word = get_random_word()


if __name__ == "__main__":
  main()


