import sys

def ListKeys():
  return True

def RemoveKey():
  return True

def AddKey():
  keyID = raw_input('Key ID: ')
  verificationCode = raw_input('Verification Code: ')

  apiKeys = open('keys.api', 'a')

  apiKeys.write(keyID)
  apiKeys.write(',')
  apiKeys.write(verificationCode)
  apiKeys.write('\n')

  apiKeys.close()

  return True
