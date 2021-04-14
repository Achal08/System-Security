from passlib.hash import sha256_crypt
print('SIGNUP\n')
username1 = input(" Enter username")
passw1 = input(" Enter pass")

print('\nLOGIN\n')
username2 = input(" Enter username")
if username1 == username2:
    passw2 = input(" Enter pass")
    password = sha256_crypt.hash(passw1)

    print('\nHashed Password\n')
    print(password)

    if (sha256_crypt.verify(passw2, password)) :
        print("Authentication Successfull")
    else :
        print("Authentication UNSuccessfull")
else:
    print('Username Incorrect')
