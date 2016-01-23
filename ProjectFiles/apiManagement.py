import sys

apiFile = 'keys.api'

def ListKeys():
  i = 0

  with open(apiFile) as apiKeys:
    for key in apiKeys:
      i += 1
      print(i)
      print key

  return True

def FormatKey(key):
  key = key.strip('\n')
  apiKey = key.split(",")
  return apiKey

def ImportISK():
  i = 0

  with open(apiFile) as apiKeys:
    for key in apiKeys:
      i += 1
      apiKey = FormatKey(key)
      print('\ncharacterName')
      print('isk amount')

  print('\ntotal isk amount')

def ImportLiquidISK():
  i = 0
  with open(apiFile) as apiKeys:
    for key in apiKeys:
      i += 1
      print('\ncharacterName')
      print('assets with isk amount')
      print('wallet amount')
      print('total isk')

  print('\ntotal wallet isk amount')
  print('total isk ammount')

def RemoveKey():
  keyToRemove = input('enter key number: ')
  with open(apiFile) as apiKeys:
    keys = apiKeys.readlines()

  keys.remove(keys[keyToRemove - 1])

  with open(apiFile, 'w') as apiKeys:
    for key in keys:
      apiKeys.write(key)

  return True

def AddKey():
  keyID = raw_input('\nKey ID: ')
  verificationCode = raw_input('Verification Code: ')

  apiKeys = open(apiFile, 'a')

  apiKeys.write(keyID)
  apiKeys.write(',')
  apiKeys.write(verificationCode)
  apiKeys.write('\n')

  apiKeys.close()

  return True
