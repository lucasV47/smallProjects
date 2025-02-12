import random
import string

def generate_pwd (min_length, numbers=True, special_char=True): # declare vars, parts of pwd to be assembled
    letters= string.ascii_letters
    digits= string.digits
    special= string.punctuation

    characters = letters # string that stores values of pwd, adding them up     
    if numbers:
       characters+= digits
    if special_char:
        characters+= special

    pwd=''
    hasNumber= False
    hasSpecial= False
    
    while len(pwd) < min_length or (numbers and not hasNumber) or (special and not hasSpecial):
        newChar= random.choice(characters) #generates letters
        pwd+= newChar

        if newChar in digits:
            hasNumber= True
        elif newChar in special:
            hasSpecial= True

    return pwd

print('\nWelcome to the password generator!')
min_length =int(input('\nEnter minimum lenght of password.\n'))
hasNumber= input('Do you want numbers in the password? (y/n)\n').lower()  == 'y'
hasSpecial=input('Do you want special caracters in the password? (y/n)\n').lower() == 'y'

pwd=generate_pwd(min_length, hasNumber, hasSpecial)
print('\nThis is the generated password: '+pwd)
