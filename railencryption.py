import numpy as np

ciphertext = "carrpyghpoyt"
depth = 5

tablematrix = [["." for i in range(len(ciphertext))] for i in range(depth)]
print(np.array(tablematrix).reshape(depth, len(ciphertext)))

dir_down = False
row, col = 0, 0
for i in range(len(ciphertext)):
    if (row == 0) or (row == depth-1):
        dir_down = not dir_down
    tablematrix[row][col] = "*"
    col +=1
    
    if dir_down:
        row += 1
    else:
        row -= 1
print(np.array(tablematrix).reshape(depth, len(ciphertext)))

index = 0 
for i in range(depth):
    for j in range(len(ciphertext)):
        if (tablematrix[i][j]=="*") and (index < len(ciphertext)):
            tablematrix[i][j] = ciphertext[index]
            index += 1
print(np.array(tablematrix).reshape(depth, len(ciphertext))) 

# reading as diagonally
row, col = 0, 0
dir_down = False
plaintext = []
for i in range(len(ciphertext)):
    if (row ==0) or (row == depth-1):
        dir_down = not dir_down
    plaintext.append(tablematrix[row][col])
    col +=1
    
    
    if dir_down:
        row +=1
    else:
        row -=1 
print(plaintext)
print("ciphertext is : "+ciphertext)
#print("depth: "+depth)
print("Plain text is : "+''.join(plaintext))
        