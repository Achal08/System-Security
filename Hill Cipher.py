import numpy as np

#input the data
data=input("Please enter the data:")
key=input("Please enter the key:")

#initialize the matrix
key_matrix=[[0 for j in range(3)] for i in range(3)]
inverse_matrix=[[0 for j in range(3)] for i in range(3)]
data_matrix=[[0] for i in range(3)]
cipher_matrix=[[0] for i in range(3)]
decrypt_matrix=[[0] for i in range(3)]

def matrix(key):
    k=0
    for i in range(0,3):
        for j in range(0,3):
            key_matrix[i][j]=ord(key[k])%65
            k=k+1

    return key_matrix

def datamatrix(data):
    for i in range(3):
        for j in range(3):
            data_matrix[i][0]=ord(data[i])%65

    return data_matrix

def encrypt(key_matrix,message_matrix):

    for i in range(3):
        for j in range(1):
            cipher_matrix[i][j]=0
            for x in range(3):
                cipher_matrix[i][j]+=key_matrix[i][x]*data_matrix[x][j]

            cipher_matrix[i][j]=cipher_matrix[i][j]%26

    return cipher_matrix


key_matrix=matrix(key)
print(key_matrix)
data_matrix=datamatrix(data)
cipher_matrix=encrypt(key_matrix,data_matrix)

cipher_text=[]
for i in range(3):
    for j in range(1):
        cipher_text.append(chr(cipher_matrix[i][j]+65))
    
print('Cipher Text:-',"".join(cipher_text))

#decrypting the text which was recieved

def inversematrix(key_matrix):
    inverse_matrix=np.linalg.inv(key_matrix)

    for i in range(3):
        for j in range(3):
            inverse_matrix[i][j]=int(inverse_matrix[i][j]%26)

    return inverse_matrix

def decrypt(cipher_matrix,inverse_matrix):

    for i in range(3):
        for j in range(1):
            decrypt_matrix[i][j]=0
            for x in range(3):
                decrypt_matrix[i][j]=inverse_matrix[i][x]*cipher_matrix[x][j]

            decrypt_matrix[i][j]=int(decrypt_matrix[i][j]%26)

    return decrypt_matrix

inverse_matrix=inversematrix(key_matrix)
print(inverse_matrix)
decrypt_matrix=decrypt(cipher_matrix,inverse_matrix)

#create a decrypt message
decrypt_message=[]

for i in range(3):
    for j in range(1):
        decrypt_message.append(chr(decrypt_matrix[i][j]+65))

print('Decrypted Message:-',"".join(decrypt_message))

