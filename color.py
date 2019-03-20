"""
 @author    : macab (macab@debian)
 @file      : color
 @created   : Wednesday Mar 20, 2019 23:18:39 IST
"""
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


# Python program to print
# green text with red background

init()
print(colored('Hello, World!', 'green', 'on_red'))


