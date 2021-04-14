"""
#Initializing variables a and b for use in recurson in #filling other characters
a = b = 0
#Getting user inputs Key (to make the 5x5 char matrix) and Plain Text (Message that is to be encripted)
key = input("Enter key: ")
key = key.replace(" ", "")
key = key.upper()
plaintext = input("Plain text: ")
plaintext = plaintext.replace(" ", "")
plaintext = plaintext.upper()
#The function matrix that creates a nested list recursively
#The nested list mimics a 5 by 5 grid, where each element in the master list
#is a list containing 5 elements itself 
def matrix (x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]
#Note to users: you can see the final generated matrix by writing in: 
#print(ciphermatrix)
#at the end of the code.

#keyintomatrix starts off as an empty list but incorporates the characters
#into the nested list matrix structure which is later appended at the start
#of the cipher matrix
keyintomatrix=list()
for c in key:
    if c not in keyintomatrix:
        if c=='J':
            keyintomatrix.append('I')
        else:
            keyintomatrix.append(c)
#this fills in the rest of the matrix with the remaining unused letters from
#the english alphabet
for i in range(65,91): 
    if chr(i) not in keyintomatrix:
        if i==73 and chr(74) not in keyintomatrix:
            keyintomatrix.append("I")
            a=1
        elif a==0 and i==73 or i==74:
            pass    
        else:
            keyintomatrix.append(chr(i))
#defining the cipher matrix as a 5x5 matrix with an inital of 0
ciphermatrix=matrix(5,5,0) 
for i in range(0,5): 
    for j in range(0,5):
        ciphermatrix[i][j]=keyintomatrix[b] #keyintomatrix being incorporated into the beginning of the cipher matrix
        b+=1
#indexlocator is a function that locates the index of a certain character
def indexlocator(x):
    lst = list()
    if x == 'J':
        x == 'I'
    for i,j in enumerate(ciphermatrix):
        for k,l in enumerate(j):
            if x == l:
                lst.append(i)
                lst.append(k)
                return lst
#encription takes in the plaintext and encripts it using the row, rectangle, or column method
#for the playfair cipher encryption method
def encription(text):
    i=0
    for s in range(0,len(text)+1,2):
        if s<len(text)-1:
            if text[s]==text[s+1]:
                text=text[:s+1]+'X'+text[s+1:]
    if len(text)%2!=0:
        text=text[:]+'X'
    print("Cipher Text: ", end=' ')
    while i < len(text):
        lst = list()
        lst = indexlocator(text[i])
        lon = list()
        lon = indexlocator(text[i + 1])
        if lst[1] == lon[1]:
            print(f"{ciphermatrix[(lst[0] + 1) %5][lst[1]]}{ciphermatrix[(lon[0] + 1) %5][lon[1]]}", end=' ')
        elif lst[0] == lon[0]:
            print(f"{ciphermatrix[lst[0]][(lst[1] + 1) %5]}{ciphermatrix[lon[0]][(lon[1] + 1) %5]}",end=' ')  
        else:
            print(f"{ciphermatrix[lst[0]][lon[1]]}{ciphermatrix[lon[0]][lst[1]]}",end=' ')    
        i += 2  
encription(plaintext)
print(ciphermatrix)
"""
#playfair cipher

key=input("Enter key: ")                                      #enter the key
key=key.replace(" ", "")                                      #the spaces are replaced, if any.
key=key.upper()                                               #the key letters are converted to uppercase for uniform key matrix formation

def matrix(x,y,initial):                                      #key matrix initialisation
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()                                                 #initialising a list with the key matrix values
for c in key: 
    if c not in result:                               
        if c=='J':                                            #this line checks if the letter is a 'J' is it is then it is replaced with an 'I' or else the letter is appended
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): 
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
            
k=0
keymatrix=matrix(5,5,0)                                       #the values of the result list is added to the keymatrix
for i in range(0,5): 
    for j in range(0,5):  
        keymatrix[i][j]=result[k]
        k+=1

def location(x): 
    loc=list()
    if x=='J':
        x='I'
    for i ,j in enumerate(keymatrix):
        for k,l in enumerate(j):
            if x==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():                                                 #function for encryption
    print(keymatrix)
    msg=str(input("Enter Plain-text:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("Cipher-Text:",end=' ')
    while i<len(msg):
        loc=list()
        loc=location(msg[i])
        loc1=list()
        loc1=location(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(keymatrix[(loc[0]+1)%5][loc[1]],keymatrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(keymatrix[loc[0]][(loc[1]+1)%5],keymatrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(keymatrix[loc[0]][loc1[1]],keymatrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
encrypt()
