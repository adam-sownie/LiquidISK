import sys
from apiManagement import *

def HandleChoiceMain(choice):
  if choice == 0:
    print('goodbye')
    sys.exit(0)

  if choice == 1:
    doAPIWork = True
    while doAPIWork:
      doAPIWork = HandleChoiceAPI(APIMenu())
    return False

  if choice == 2:
    return True

  print('Please choose an option from the list\n')
  return False

def PrintMenu():
  print('0) exit')
  print('1) manage API keys')
  print('2) refresh wallets\n')

  choice=input(': ')

  return choice

def HandleChoiceAPI(choice):
  if choice == 0:
    print('returning to main menu\n')
    return False

  if choice == 1:
    return ListKeys()

  if choice == 2:
    return AddKey()

  if choice == 3:
    return RemoveKey()

  print('Please choose an option from the list\n')
  return False

def APIMenu():
  print('0) exit API magement')
  print('1) list keys')
  print('2) add key')
  print('3) remove key\n')

  choice=input(': ')

  return choice
