# Citrix CTX1 decryptor

def decrypt_letters(letters, v = 0):
  f = (ord(letters[2]) - 1) & 0x0f
  s = (ord(letters[3]) - 1) & 0x0f
  return chr((f*16+s) ^ v)

def decrypt(password):

  clear = ""
  v = 0

  for i in range(0, len(password), 4):
    c = decrypt_letters(password[i:i+4], v)
    v = v ^ ord(c)
    clear += c
  return clear

decrypt("NFHALEBBMHGCLEBBMDGGKMAJNOHLLKBP")
# Decrypts to 'password'