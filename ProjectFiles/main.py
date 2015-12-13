import sys
from menu import *

userChoice = 99

while True:
 userChoice = PrintMenu()
 HandleChoice(userChoice)
 print('\n')
