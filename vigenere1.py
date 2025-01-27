plaintext = "YOUTUBE"
key = "MEC"
plaintext = plaintext.replace(" ","")
plaintext = plaintext.lower()

key = key.lower()

print(plaintext)

keyextend = []
index = 1
while index<=len(plaintext):
    for i in key:
        if index <= len(plaintext):
            keyextend.append(i)
            index +=1
print(''.join(keyextend))

ciphertext = []

for i in range(len(plaintext)):
    ciphertext += chr((ord(plaintext[i])-97 + ord(keyextend[i])-97)%26+97)
print(ciphertext)



