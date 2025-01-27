#hill cipher
#python -m venv my_env
# .\my_env\Scripts\activate
#pip install numpy
import numpy as np
import math as mt

PT = "Pay More Money"
key = "rrfvsvcct"
PT = PT.replace(" ","")
PT = PT.lower()
print(PT)
# dictinary making
chartoNumber = {chr(i):i-97 for i in range(97,123)}
numbertoChar = {i-97:chr(i) for i in range(97,123)}
print(chartoNumber)
print(numbertoChar)

keyintoNumber = [chartoNumber[c] for c in key]
PTNumber = [chartoNumber[c] for c in PT]
print(keyintoNumber)
print(PTNumber)

BL = round(mt.sqrt(len(key)))

print(BL)

keyMatrix = np.array(keyintoNumber).reshape(BL,BL)

print(keyMatrix)

PTarray = np.array(PTNumber)

print(PTarray)

PTBlock = np.split(PTarray, len(PTNumber)/BL)
print(PTBlock)

CTBlock = [np.matmul(PTBlock[i], keyMatrix)%26 for i in range(len(PTBlock))]
print(CTBlock)

CTNumber = np.concatenate(CTBlock)
print(CTNumber)

CT = [numbertoChar[i] for i in CTNumber]
CT = "".join(CT)
print(CT)

# decryption of hill cipher started
# we already have CT, CTblock, keymatrix
print(CT)
print(CTBlock)
print(keyMatrix)
# PT_block = ?
'''
PT = CT*k^-1%26
k_inv = 1/det_k * adj_k
adj_k = k_inv * det_k % 26
k_inv = np.linalg.inv(keyMatrix)
det_k = round(np.linalg.det(keyMatrix))
'''
k_inv = np.linalg.inv(keyMatrix)
k_det = round(np.linalg.det(keyMatrix))
print(k_inv)
print(k_det)

adj_k = k_inv*k_det % 26
print(adj_k)

k_det_mul_inv = pow(k_det,-1, 26)
print(k_det_mul_inv)

key_matr_mul_inv = k_det_mul_inv * adj_k % 26
print(key_matr_mul_inv)

PT_block = [np.matmul(CTBlock[i],key_matr_mul_inv)%26 for i in range(len(CTBlock))]
print(PT_block)
PT_list = np.concatenate(PT_block)
print(PT_list)

PT = ""
for i in PT_list:
    if round(i)==26:
        PT += numbertoChar[0]
    else:
        PT += numbertoChar[round(i)]
print(PT)
print(CT)