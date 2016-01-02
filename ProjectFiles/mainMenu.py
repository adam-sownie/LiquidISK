import sys
import apiMenu
import walletHandler

def HandleChoiceMain(choice):
  if choice == 0:
    print('goodbye')
    sys.exit(0)

  if choice == 1:
    doAPIWork = True
    while doAPIWork:
      doAPIWork = apiMenu.HandleChoiceAPI(
                    apiMenu.PrintAPIMenu())
    return doAPIWork

  if choice == 2:
    return walletHandler.ShowISK()

  print('Please choose an option from the list')
  return False

def PrintMenu():
  print('\n0) exit')
  print('1) manage API keys')
  print('2) refresh wallets\n')

  choice = input(': ')

  return choice
