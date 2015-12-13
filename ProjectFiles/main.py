import sys
from menus import *

userChoice = 99

while True:
 userChoice = PrintMenu()
 HandleChoice(userChoice)
 print('\n')
