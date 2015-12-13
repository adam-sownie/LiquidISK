from apiManagement import *

def PrintMenu():
  print('1) exit')
  print('2) manage API keys')
  print('3) refresh wallets')
  choice=input(': ')
  return choice

def APIMenu():
  return False

def Chosen(choice):
  if choice in [1, 2, 3]:
    return True

  print('please choose an option')
  return False
