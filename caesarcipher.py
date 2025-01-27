# for encryption

def encryption(PT, key):
    CT = ""
    for c in PT:
        if c.islower():
            CT += chr((ord(c)+key-97)%26+97)
        elif c.isupper():
            CT += chr((ord(c)+key-65)%26+65)
        else:
            CT += c
    return CT

# for decryption
def decryption(CT, key):
    PT = ""
    for c in CT:
        if c.islower():
            PT += chr((ord(c)-key-97)%26+97)
        elif c.isupper():
            PT += chr((ord(c)-key-65)%26+65)
        else:
            PT += c
    return PT

plaintext = input("Enter plain text: ")
key = int(input("Enter the key: "))
ciphertext = encryption(plaintext, key)
print(ciphertext)

ciphertext = input("Enter cipher text: ")
key = int(input("Enter the key value: "))
plaintext = decryption(ciphertext, key)
print(plaintext)
