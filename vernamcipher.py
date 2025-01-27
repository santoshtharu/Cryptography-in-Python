plaintext = "helloworld"
key = "mahendra"

numbertochar = {i-97:chr(i) for i in range(97,123)}
print(numbertochar)

chartonumber = {chr(i):i-97 for i in range(97,123)}
print(chartonumber)

plaintextnumber = [chartonumber[i] for i in plaintext]
print(plaintextnumber)
keynumber = [chartonumber[i] for i in key]
print(keynumber)

if len(plaintext)>len(key):
    k = len(plaintext) - len(key)
    for i in range(k):
        keynumber.append(0)
else:
    k = len(key) - len(plaintext)
    for i in range(k):
        plaintextnumber.append(0)

print(" _____ after padding _______")
print(plaintextnumber)
print(keynumber)

xorresult = []
for i in range(len(plaintextnumber)):
    xorresult.append((plaintextnumber[i] ^ keynumber[i])%26)

print(xorresult)

cipherlist = [numbertochar[i] for i in xorresult]

print(cipherlist)
print(plaintext)
print(key)
print(''.join(cipherlist))


    

