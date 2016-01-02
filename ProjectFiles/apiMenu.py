from apiManagement import *

def HandleChoiceAPI(choice):
  if choice == 0:
    print('returning to main menu')
    return False

  if choice == 1:
    return ListKeys()

  if choice == 2:
    return AddKey()

  if choice == 3:
    return RemoveKey()

  print('Please choose an option from the list')
  return False

def PrintAPIMenu():
  print('\n0) exit API magement')
  print('1) list keys')
  print('2) add key')
  print('3) remove key\n')

  choice = input(': ')

  return choice
