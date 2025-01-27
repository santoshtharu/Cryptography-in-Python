# vigenere cipher
plaintext = "youtube"
key = "mec"
# plaintext = key (in terms of length)

keyextend = []

index = 1
while index <= len(plaintext):
    for i in key:
        if index <= len(plaintext):
            keyextend.append(i)
            index += 1
print("Repeated Key is: "+''.join(keyextend))
print("Plain text: "+plaintext)

ciphertext = []
for i in range(len(plaintext)):
    ciphertext.append(chr(
        ((ord(plaintext[i])-97) + (ord(keyextend[i])-97))%26+97
    ))
print("Cipher text is :"+''.join(ciphertext))

# Autokey system
# key = plaintext (in terms of length)
# key is not repeated, plaintext is appended behind the key to make equal length

print("____ auto key system started ______")
plaintext = "youtube"
key = "mec"

keyextend = []

for i in key:
    keyextend.append(i)

while len(keyextend) < len(plaintext):
    for i in plaintext:
        if len(keyextend) < len(plaintext):
            keyextend.append(i)
print(keyextend)
print(key)
print(plaintext)

ciphertext = []

for i in range(len(plaintext)):
    ciphertext.append(chr(
        ((ord(plaintext[i])-97) + (ord(keyextend[i])-97))%26+97
    ))

print(ciphertext)

# vernam cipher 
# xor operation on plaintext and key
# length of key = length of plaintext
print("__________ vernam cipher started ________")
plaintext = "youtube"
key = "abcdefh" # must not repeat any letter in key, otherwise decryption will be wrong

ciphertext = []
for i in range(len(plaintext)):
    ciphertext.append(chr(
        ((ord(plaintext[i])-97) ^ (ord(key[i])-97))%26+97
    ))
print(plaintext)
print(key)
print(ciphertext)

# One time pad (OTP)
# key is randomly  auto-generated, 
import random
print("____ one time pad started _____")

plaintext = "youtube"
length = len(plaintext)

key = ""
for i in range(length):
    key += random.choice("abcdefghijklmnopqrstuvwxyz")
print(key)

ciphertext = []
for i in range(length):
    ciphertext.append(chr(
        ((ord(plaintext[i])-97) ^ (ord(key[i])-97))%26+97
    ))
print(plaintext)
print(ciphertext)