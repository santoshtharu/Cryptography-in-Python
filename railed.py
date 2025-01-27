import numpy as np

PT = "cryptography"
CT = "carrpyghpoyt"
depth = 5

def encryption(text, depth):
    CT = []
    # first of all make a table matrix
    tablematrix = [["." for i in range(len(text))] for i in range(depth)]
    print(np.array(tablematrix).reshape(depth, len(text)))
    
    row, col = 0, 0
    dir_down = False
    for i in range(len(text)):
        if (row==0) or (row==depth-1):
            dir_down = not dir_down
        tablematrix[row][col] = text[i]
        col +=1
        if dir_down:
            row += 1
        else:
            row -= 1
    print(np.array(tablematrix).reshape(depth, len(text)))
    
    for i in range(depth):
        for j in range(len(text)):
            if tablematrix[i][j]!=".":
                CT.append(tablematrix[i][j])
      
    return ''.join(CT)

def decryption(ciphertext, depth):
    tablematrix = [["." for i in range(len(ciphertext))] for i in range(depth)]
    print(np.array(tablematrix).reshape(depth, len(ciphertext)))
    dir_down = False
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if (row==0) or (row==depth-1):
           dir_down = not dir_down
        
        tablematrix[row][col]= "*"
        col += 1
        if dir_down:
            row +=1
        else:
            row -=1
    print(np.array(tablematrix).reshape(depth, len(ciphertext)))
    index = 0
    for i in range(depth):
        for j in range(len(ciphertext)):
            if (tablematrix[i][j] == "*") and (index < len(ciphertext)):
                tablematrix[i][j] = ciphertext[index]
                index += 1
    print(np.array(tablematrix).reshape(depth, len(ciphertext)))
    PT = []
    row, col = 0, 0
    dir_down = False
    
    for i in range(len(ciphertext)):
        if (row==0) or (row == depth-1):
            dir_down = not dir_down
        PT.append(tablematrix[row][col])
        col +=1
        if dir_down:
            row +=1
        else:
            row -=1
    print(PT)
                
        
    
    return ''.join(PT)

# print(encryption(PT, depth))

print(decryption(CT, depth))