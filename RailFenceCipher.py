def encryptr_f(text, key):
 r = [['\n' for i in range(len(text))]
      for j in range(key)]
 dir_down = False
 row, col = 0, 0
 for i in range(len(text)):
     if (row == 0) or (row == key - 1):
         dir_down = not dir_down
     r[row][col] = text[i]
     col += 1
     if dir_down:
         row += 1
     else:
         row -= 1
 result = []
 for i in range(key):
     for j in range(len(text)):
         if r[i][j] != '\n':
             result.append(r[i][j])
 return("" . join(result))


def decryptr_f(cipher, key):
 r = [['\n' for i in range(len(cipher))]
      for j in range(key)] 
 dir_down = None
 row, col = 0, 0
 for i in range(len(cipher)):
     if row == 0:
         dir_down = True
     if row == key - 1:
         dir_down = False
     r[row][col] = '*'
     col += 1
     if dir_down:
         row += 1
     else:
         row -= 1
 index = 0
 for i in range(key):
     for j in range(len(cipher)):
         if ((r[i][j] == '*') and
         (index < len(cipher))):
             r[i][j] = cipher[index]
             index += 1
 result = []
 row, col = 0, 0
 for i in range(len(cipher)):
     if row == 0:
         dir_down = True
     if row == key-1:
         dir_down = False
     if (r[row][col] != '*'):
         result.append(r[row][col]) 
         col += 1
     if dir_down:
         row += 1
     else:
         row -= 1
 return("".join(result))


str1=input("Enter Plain Text:")
k=int(input("Enter key:"))
encrypt=encryptr_f(str1,k)
decrypt=decryptr_f(encrypt,k)
print("your encrypted text is")
print(encrypt)
print("your decrypted text is")
print(decrypt)
