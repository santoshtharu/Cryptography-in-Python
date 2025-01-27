import random

def generateRandomkey(keylength):
    key = ""
    for i in range(keylength):
        key += random.choice("abcdefghijklmnopqrstuvwxyz")
    return key
print(generateRandomkey(5))

def encryption(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(((ord(plaintext[i])^ord(key[i])-97)%26+97))
    return ciphertext
#print(encryption("hello", generateRandomkey(5)))
print(encryption("hello", "cello"))
def decryption(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i])^ord(key[i]))
    return plaintext
print(decryption("hello", "cello"))

   