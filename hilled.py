import numpy as np
import math as ma

# key-value pair - dictionary
chartonumber = {chr(i):i-97 for i in range(97,123)} # lowercase letter 
numbertochar = {i-97:chr(i) for i in range(97,123)} # lowercase letter

print(chartonumber)
print(numbertochar)

PT="Pay More Money"
key = "rrfvsvcct"

PT = PT.replace(" ","")
PT = PT.lower()

PT_number = [chartonumber[i] for i in PT] # list of plain text into number
key_number = [chartonumber[i] for i in key] # list of key into number
print(PT_number)
print(key_number)

# check given matrix is square or not
BL = round(ma.sqrt(len(key_number)))
print(BL)

key_matrix = np.array(key_number).reshape(BL, BL) # reshaping matrix size 3x3
print(key_matrix)

PT_array = np.array(PT_number)
print(PT_array)

PT_block = np.split(PT_array,len(PT_array)/BL)
print(PT_block)
#now starting multiplication as per the encryption algorithm
# CT = PT * K % 26
# CT = matrix in result
# PT = matrix
# K = a square matrix

CT_block = [np.matmul(PT_block[i],key_matrix)%26 for i in range(len(PT_block))]
print(CT_block)

CT_array = np.concatenate(CT_block)
print(CT_array) 

# changing number into character
CT_list = [numbertochar[i] for i in CT_array]

print(CT_list)
CT = ''.join(CT_list)
print("plaintext: ", PT)
print("Cipher text: ", CT)
# now decryption started

'''
we already have 
Cipher text
key_matrix
plain text = ? 
PT = CT*K^-1%26
where K^-1 is multiplicative inverse matrix of key_matrix
key_matrix_inverse = 1/det_key_matrix * adj_key_matrix ---- (i)
adj_key_matrix = key_matrix_inverse * det_key_matrix --- (ii)
'''
print(key_matrix)
key_matrix_inverse = np.linalg.inv(key_matrix)
det_key_matrix = round(np.linalg.det(key_matrix))
print(key_matrix_inverse)
print(det_key_matrix)

adj_key_matrix = key_matrix_inverse * det_key_matrix % 26
print(adj_key_matrix)

det_key_matrix_mul_inverse = pow(det_key_matrix, -1, 26)
print(det_key_matrix_mul_inverse)

mul_inv_key_matrix = det_key_matrix_mul_inverse * adj_key_matrix % 26
print(mul_inv_key_matrix)

PT_block = [np.matmul(CT_block[i], mul_inv_key_matrix)% 26 for i in range(len(CT_block))]
print(PT_block)

PT_list = np.concatenate(PT_block)
print(PT_list)
CT = []

for i in PT_list:
    if round(i)==26:
        CT += [numbertochar[0]]
    else:
        CT += [numbertochar[round(i)]]
print(''.join(CT))

