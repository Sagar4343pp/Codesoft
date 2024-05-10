import random
import string

def password_generator(length, complexity):
    if complexity == 'simple':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation 
    elif complexity == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    else:
        print("Invalid complexity level")

    password = ''.join(random.choice(characters) for _ in range(length))
    return (f'Password: {password}')

length = int(input('Enter your Passwword Length'))
complexity = (input('Enter complexity Level..... (simple/medium/hard):  '))

print(password_generator(length, complexity))


