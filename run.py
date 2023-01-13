import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

name = None
name = input(f"{Fore.RED+Style.BRIGHT}What is your name?")
print(name)
