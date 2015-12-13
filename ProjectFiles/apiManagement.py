def ListKeys():
  return True

def RemoveKey():
  return True

def AddKey():
  return True
  keyID=input('  KeyID: ')
  verificationCode=input('  verificationCode: ')

  apiKeys = open('\\APIKeys\\keys.api', 'a')

  apiKeys.write(keyID)
  apiKeys.write(verificationCode)

  apiKeys.close()

  return True
