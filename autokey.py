plaintext = "YOUTUBE"
key = "MEC"
plaintext = plaintext.replace(" ","")
plaintext = plaintext.lower()

key = key.lower()

print(plaintext)

keyextend = []
for i in key:
    keyextend.append(i)
index = len(keyextend)
while len(keyextend)<len(plaintext):
    for i in plaintext:
        if len(keyextend) < len(plaintext):
            keyextend.append(i)
            #index +=1
print(''.join(keyextend))

ciphertext = []

for i in range(len(plaintext)):
    ciphertext += chr((ord(plaintext[i])-97 + ord(keyextend[i])-97)%26+97)
print(ciphertext)



