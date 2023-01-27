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
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
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


def game_start():

    """
    Instructions for game
    """
    print(Fore.GREEN + welcome)
    sleep(1)

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
    return word.lower()


def hangman_play():
    """
    Display output for each word, guess rigth letter
    """

    word = get_random_word()
    word_completion = "_" * len(word)
    game_won = False
    correct_letters = []
    guessed_wrong = []
    guessed_words = []
    lives = 7
    print(word_completion)

# geussing letters in a secred word, all guess full word and win
    while not game_won and lives > 0:
        guess = input("Please enter a letter or word:").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in correct_letters or guess in guessed_wrong:
                print(f"{Fore.RED+Style.BRIGHT}You already guessed\n"
                      "the letter", guess)

        elif guess not in word:
            print(guess, f"{Fore.RED+Style.BRIGHT}is not in the word")
            lives -= 1
            guessed_wrong.append(guess)
            print(f"You have left: {lives}")
        else:
            print(f"{Fore.GREEN+Style.BRIGHT}Good job!\n", guess,
                  "is in the word!")
            correct_letters.append(guess)
            output = list(word_completion)
            blank = [i for i, letter in enumerate(word) if letter == guess]
            for index in blank:
                output[index] = guess
            word_completion = "".join(output)
            if "_" not in word_completion:
                game_won = True
            #    break
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print(f"{Fore.GREEN+Style.BRIGHT}You already\n"
                          "guess the word", guess,)
            elif guess != word:
                print(guess, "is not the word.")
                lives -= 1
                guessed_words = word
            else:
                game_won = True
                word_completion = word
    else:
        print("Incorrect guess")
    print(display_hangman(lives))
    print(word_completion)
    print("/n")
    if game_won:
        print("Congratulation,you gueesed the word!You win")
        print()
    else:
        print("Sorry ,you run out of\n" 
              "lives.The word was" + word + "Try play again")


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
if __name__ == "__main__": 
    main()