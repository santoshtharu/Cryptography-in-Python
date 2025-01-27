#decryption for caesar cipher

CT = "Khoor"
key = 3
PT = ""

for c in CT:
    if c.islower():
        PT += chr((ord(c)-key-97)%26+97)
    elif c.isupper():
        PT += chr((ord(c)-key-65)%26+65)
    else:
        PT += c
print("Cipher text: "+CT)
print("Plain text: "+PT)