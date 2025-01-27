#caesar cipher Encryption

#print(ord("a"))
#print(ord("A"))

PT = input("Enter plaint text: ")
key = 3
CT= ""

for c in PT:
    if c.islower():
        CT += chr((ord(c)+key-97)%26+97)
    elif c.isupper():
        CT += chr((ord(c)+key-65)%26+65)
    else:
        CT += c
print("Plain text: "+PT)        
print("Cipher text:" +CT)