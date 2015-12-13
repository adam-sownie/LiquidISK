def PrintMenu():
  print('1) add API')
  print('2) refresh wallets')
  choice=input(': ')
  return choice

def Chosen(choice):
  if choice == 1:
    return True

  elif choice == 2:
    return True

  print('please choose an option')
  return False
