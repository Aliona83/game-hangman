import  colorama
from colorama import Fore, Style
  
def welcome_user():
   name = input(f"{Fore.RED+Style.BRIGHT}What is your name?\n") 
   print(name)