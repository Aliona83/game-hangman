import random
from words import words
from time import sleep
import os
import colorama

from colorama import Fore, Style

from graffiti import welcome, win, lose

return_back = 0
word = ""
colorama.init(autoreset=True)


def display_hangman(lives):

    """
    Structure for Hangman display
    """
    hangman = [ '''
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


def game_start():

    """
    Instructions for game
    """
    print(Fore.GREEN + welcome)
    # sleep(1)

    print("Welcome Dear Friend! It is time for game.\n")
    name =''
    while True:
        name = input("Please enter your name(use letters only):")
        if not name.isalpha():
          print("Enter only letters")
          continue
        else:
            print(f"{Fore.YELLOW+Style.BRIGHT}Hello" + " " + name,)
            break
     

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
    global word
    word = random.choice(words)
    print(word)
    return word.lower()


def hangman_play():
    """
    Display output for each word, guess rigth letter
    """

    word = get_random_word()
    word_completion = "-" * len(word)
    output = list(word_completion)
    game_won = False
    guessed_letters = []
    guessed_already = []
    guessed_words = []
    lives = 7
    hang_position = 0
    print(word_completion)
    global return_back

# guessing letters in a secred word, all guess full word and win
    while not game_won and lives > 0:
        if lives == 0:
            return_back = 1
        
        guess = input("Please enter a letter or word:").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters or guess in guessed_already:
                print(f"{Fore.RED+Style.BRIGHT}You already guessed\n"
                      "the letter", guess)

            elif guess  in word:
                 guessed_letters.append(guessed_letters)
                 print(f"{Fore.GREEN+Style.BRIGHT}Well done! this letter is in the word")
                 if guess not in guessed_already:
                      guessed_already.append(guess)
            else:
                print(f"{Fore.RED+Style.BRIGHT}Ooops,you lost 1 life!\n", lives, "remaining")
                print("Letter:", guess, f"{Fore.RED+Style.BRIGHT}is not the word.")
                print(display_hangman(hang_position))
                lives -= 1
                hang_position += 1

            
        elif guess not in word:
             print(guess,f"{Fore.GREEN+Style.BRIGHT} is in the word!")  
             lives -= 1
             hang_position += 1
             print(word_completion = "".join(output))
        else:   
            guessed_letters.append(guess)
            blank = [i for i, letter in enumerate(word) if letter == guess]
            for index in blank:
                 output[index] = guess
            word_completion = "".join(output)
            if "-" not in word_completion:
                game_won = True
            elif len(guess) == len(word) and guess.isalpha():
                    print(f"{Fore.GREEN+Style.BRIGHT}You already\n"
                          "guess the word", guess,)
            elif guess != word:
                lives -= 1
                hang_position += 1
                # guessed_words = word
            else:
                game_won = True
                word_completion = word
    else:
        print("Incorrect guess")
    print("/n")
    if game_won:
        print("Congratulation,you guessed the word!You win")
        print(Fore.GREEN + win)
        print(play_loop())
        print()
    else:
        print("Sorry ,you run out of \n"
              "lives.The word was"  +  word  + ".Try play again")
        print(Fore.RED + lose)
        return_back = 1
        print(play_loop())

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def play_loop():
    
  global play_again
  play_again = input("Do you want to play again? y=yes,n=no\n")
  while play_again not in ["y", "n", "Y", "N"]:
    play_again = input("Do you want to play again? y =yes, n = no\n")
  if play_again == "y":
    clear()
    main()
  elif play_again == "n":
    print("Thanks for playing! We expect you back again!")


def main():
    """
    Function to return a game from beginning
    """
    game_start()
    play_again = 1
    while return_back != 1 and play_again == 1:
     hangman_play()
     play_loop()
    return 0    

main()