from apiManagement import *

def PrintMenu():
  print('1) exit')
  print('2) manage API keys')
  print('3) refresh wallets\n')

  choice=input(': ')

  return choice

def APIMenu():
  print('1) list keys')
  print('2) remove key')
  print('3) add key\n')

  choice=input(': ')

  return choice

def Chosen(choice):
  if choice in [1, 2, 3]:
    return True

  print('please choose an option')
  return False
