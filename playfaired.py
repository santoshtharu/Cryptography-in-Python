import numpy as np
#playfair cipher
PT = "mosque"
key = "monarchy"

PT = PT.replace(" ","")
PT = PT.lower()
print(PT)
print(key)
def makeDiagraph(text):
    list = []
    for i in range(0, len(text), 2):
        list.append(text[i:i+2])
    return list

print(makeDiagraph(PT))

def addFillerLetter(text):
    k = len(text)
    if k%2==0:
        for i in range(0, k, 2):
          if text[i] == text[i+1]:
              new_word = text[0:i+1]+str('x')+text[i+1:]
              new_word = addFillerLetter(new_word)
              break
          else:
              new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1]+str('x')+text[i+1:]
                new_word = addFillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word
print(addFillerLetter(PT)) 

plaintextlist = makeDiagraph(addFillerLetter(PT))
print(plaintextlist)

if plaintextlist[-1]!=2:
    plaintextlist[-1] = plaintextlist[-1]+str('x')

print(plaintextlist)

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate5x5Matrix(list, key):
    uniquekey = []
    for i in key:
        if i not in uniquekey:
            uniquekey.append(i)
    matrixlist = []
    for i in uniquekey:
        if i not in matrixlist:
            matrixlist.append(i)
    for i in list:
        if i not in matrixlist:
            matrixlist.append(i)
    matrix = []
    while matrixlist!=[]:
        matrix.append(matrixlist[0:5])
        matrixlist = matrixlist[5:]
    return matrix
print(np.array(generate5x5Matrix(list1, key)).reshape(5,5))
matrix = generate5x5Matrix(list1, key)
print(matrix)
def searchElement(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j
print(searchElement(generate5x5Matrix(list1, key), 'z'))

def rowRule(matrix, e1r, e1c, e2r, e2c):
    c1 = ''
    c2 = ''
    if e1c ==4:
        c1 = matrix[e1r][0]
    else:
        c1 = matrix[e1r][e1c+1]
    if e2c ==4:
        c2 = matrix[e2r][0]
    else:
        c2 = matrix[e2r][e2c+1]
    return c1, c2

def columnRule(matrix, e1r, e1c, e2r, e2c):
    c1 = '' 
    c2 = ''
    if e1r == 4:
        c1 = matrix[0][e1c]
    else:
        c1 = matrix[e1r+1][e1c]
    if e2r == 4:
        c2 = matrix[0][e2c]
    else:
        c2 = matrix[e2r+1][e2c]
    return c1, c2
def rectangleRule(matrix, e1r, e1c, e2r, e2c):
    c1 = matrix[e1r][e2c]
    c2 = matrix[e2r][e1c]
    return c1, c2

print(rectangleRule(matrix, 0,0,4,4))
print(rowRule(matrix, 0,0,0,4))
print(columnRule(matrix,1,4,4,4))

def encryptionPlayfair(matrix, plaintextlist):
    c1, c2 = 0, 0
    ciphertextlist = []
    for i in range(0,len(plaintextlist)):
        e1r, e1c = searchElement(matrix, plaintextlist[i][0])
        e2r, e2c = searchElement(matrix, plaintextlist[i][1])
        
        if e1r == e2r:
            c1, c2 = rowRule(matrix, e1r, e1c, e2r, e2c)
        elif e1c == e2c:
            c1, c2 = columnRule(matrix, e1r, e1c, e2r, e2c)
        else:
            c1, c2 = rectangleRule(matrix, e1r, e1c, e2r, e2c)
        cipher = c1 + c2
        ciphertextlist.append(cipher)
    return ''.join(ciphertextlist)
print(encryptionPlayfair(matrix, plaintextlist))
        