import numpy as np
import math as ma

# dictionary for key=value pair for number to char and char to number
numbertochar = {i-97:chr(i) for i in range(97,123)}
chartonumber = {chr(i):i-97 for i in range(97,123)}

PT = "Pay More Money"
key = "dfdg"
PT =  PT.replace(" ","")
PT = PT.lower()

# encryption 
print("--------------Encryption started------------------")
# converting plaintext into number format in list data structure
PT_number = [chartonumber[i] for i in PT]
print(PT_number)
#converting key into number list data structure
key_number = [chartonumber[i] for i in key]
print(key_number)

BL = round(ma.sqrt(len(key_number)))
print(BL)

key_matrix = np.array(key_number).reshape(BL, BL)
print(key_matrix)
PT_array = np.array(PT_number)

PT_block = np.split(PT_array,len(PT_number)/BL)
print(PT_block)

CT_block = [np.matmul(PT_block[i], key_matrix)%26 for i in range(len(PT_block))]
print(CT_block)

CT = []
CT_number = np.concatenate(CT_block)
print(CT_number)

CT = [numbertochar[i] for i in CT_number]
print("".join(CT))

#decryption started

print("___________Decryption started ____________")
# find inverse matrix multiplication
# K_inverse_matrix = 1/det_Kmat * adj_K
# adj_k = K_inverse_matrix * det_Kmat

K_inverse_matrix = np.linalg.inv(key_matrix)
print(K_inverse_matrix)

det_Kmat = round(np.linalg.det(key_matrix))
print(det_Kmat)

adj_k = K_inverse_matrix * det_Kmat %26
print(adj_k)

adj_k_inverse = pow(det_Kmat, -1, 26)
print(adj_k_inverse)

mat_mul_inverse = adj_k_inverse * adj_k % 26
print(mat_mul_inverse)

PT_block = [np.matmul(CT_block[i], mat_mul_inverse)%26 for i in range(len(CT_block))]
print(PT_block)

PT_number = np.concatenate(PT_block)
print(PT_number)

PT = []
for i in PT_number:
    if round(i) ==26:
        PT += numbertochar[0] 
    else:
        PT += numbertochar[round(i)]
print("".join(PT))
