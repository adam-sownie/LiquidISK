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

def RemoveKey():
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
