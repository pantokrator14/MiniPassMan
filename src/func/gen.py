import random

import bcrypt

def generator():
    lower = 'abcdefghijklmnñopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    numero = '0123456789'
    alfanum = '*/-_()=.,'

    todo = lower + upper + numero + alfanum 
    largo = int(input("¿Qué tan larga quieres que sea la contraseña?: "))
    
    password = "".join(random.sample(todo, largo))
    print("tu contraseña es: " + password)
    return password

def salt(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def check(password, hashedpw):
    return bcrypt.checkpw(password, hashedpw)