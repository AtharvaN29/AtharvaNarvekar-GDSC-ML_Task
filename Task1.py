import random  #as we are using the "random" function

 #can add multiple list of chars to make the password more secure
chars1="abcdefghijklmnopqrstuvwxyz" 
chars2=chars1.upper()
chars3="!@#$%^&*()"
chars=chars1+chars2+chars3

while 1:
    password_len= int(input("length of the password:"))
    password_count= int(input("no of passwords you want:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char=random.choice(chars)
            password = password + password_char
        print("the passsword is:",password)