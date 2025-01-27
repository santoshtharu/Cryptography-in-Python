import random

def generateRandomKey(keylenght):
    key = ""
    for i in range(keylenght):
        key += random.choice("abcdefghijklmnopqrstuvwxyz")
    return key 


def encryption(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr((((ord(plaintext[i])^ ord(key[i])-97)%26)+97))
    return ciphertext

PT = "hello"
keylength = len(PT)
print("plaintext: "+PT)
key = generateRandomKey(keylength)
print("key: "+key)
print("ciphertext: "+encryption(PT, key))
