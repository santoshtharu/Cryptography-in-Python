import random

plaintext = "ab"
keylength = len(plaintext)

def generateRandomkey(keylength):
    key = ""
    for i in range(keylength):
        key += random.choice("abcdefghijklmnopqrstuvwxyz")
    return key

key = generateRandomkey(keylength)
print(key)

def encryption(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(
            ((ord(plaintext[i]) -97)^ (ord(key[i]) -97))%26+97
        )
    return ciphertext
print(encryption(plaintext, key))