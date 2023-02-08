import random
from words import words, hangman
from time import sleep
import os
import colorama

from colorama import Fore, Style

from graffiti import welcome, win, lose

return_back = 0
word = ""
colorama.init(autoreset=True)


def game_start():

    """
    Instructions for game
    """
    print(Fore.GREEN + welcome)
    sleep(1)

    print("Welcome Dear Friend! It is time for game.\n")
    name = ''
    while True:
        name = input("Please enter your name(use letters only):")
        if not name.isalpha():
            print("Enter only letters")
            continue
        else:
            print(f"{Fore.YELLOW+Style.BRIGHT}Hello" + " " + name,)
            break
        sleep(1)

    print("--------------------------------------")
    sleep(1)
    print(f"{Fore.BLUE+Style.BRIGHT}GAME RULES:")
    sleep(1)
    print(
        "1.You have to guess the secret word one letter at a time \n"
        "before you are out of lives.\n"
      )
    sleep(1)
    print(
        "2.After each incorrectly answered \n"
        "letter your Hangman will start to  build.\n"
      )
    sleep(1)
    print(f"3. {Fore.RED+Style.BRIGHT}You have only 7 tries")
    print()
    print(
        "When you reach 0 lives. You will be Hanged!\n"
        "Don't worry you can restart the game!"
      )
    sleep(1)
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

    return word.lower()


def hangman_play():
    """
    Display output for each word, guess rigth letter
    """
    word = get_random_word()
    display = "-" * len(word)
    print(display)
    game_won = False
    guessed_already = []
    lives = len(hangman)
    hang_position = 0
    global return_back

    guess = ""
    while not game_won and lives > 0:
        guess = input("Enter only  single letter no numbers :").lower()
        if len(guess) == 1 and guess.isalpha():
            print(guess)
        else:
            print("This is not a single letter")
            continue
        i = 0
        if guess in word:
            while word.find(guess, i) != -1:      
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
                print(display)
                print(f"{Fore.GREEN+Style.BRIGHT}Well done!\n" 
                      "this letter is in the word")
        if guess not in word:
            print(guess, f"{Fore.RED+Style.BRIGHT} is not the word!")
            print(f"{Fore.RED+Style.BRIGHT}LEFT:\n", lives)
            print(hangman[7-lives])
            lives -= 1

        if word == display:
            print("Congratulation, You win!")
            print(Fore.GREEN + win)
            game_won = True
        if lives == 0:
            print(Fore.RED + lose)
            game_won = True
            print(f"{Fore.CYAN+Style.BRIGHT}THE WORD WAS ", word)
            print()
            sleep(3)


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
    if play_again == "n":
        print("Thanks for playing! We expect you back again!")
        quit()


def main():
    """
    Function to return a game from beginning
    """
    game_start()
    # play_again = 1
    # while return_back != 1 and play_again == 1:
    hangman_play()
    play_loop()
    return 0


main()