import sys
from apiManagement import *

def HandleChoice(choice):
  if choice == 0:
    print('goodbye')
    sys.exit(0)

  if choice == 1:
    APIMenu()

  if choice == 2:
    return True

  return False

def PrintMenu():
  print('0) exit')
  print('1) manage API keys')
  print('2) refresh wallets\n')

  choice=input(': ')

  return choice

def APIMenu():
  print('1) list keys')
  print('2) remove key')
  print('3) add key\n')

  choice=input(': ')

  return choice

def Chosen(choice):
  if choice in [0, 1, 2]:
    return True

  print('please choose an option')
  return False
