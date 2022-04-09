import imp
from os import system, name 
from time import sleep

#nos permite limpiar la terminal al iniciar cada pantalla
def clear():
    #windows
    if name == 'nt':
        _ = system('cls') #Realmente podria nombrarla como sea, pero como por defecto python usa el piso por defecto, pues...
    #UNIX
    else:
        _ = system('clear')


#Menu inicial del sistema
def menu():
    clear() #Primero limpiamos

    print('¿Qué quieres hacer?')
    print('1. Guardar nueva contraseña.')
    print('2. Mostrar contraseñas guardadas.')
    print('3. Modificar datos')
    print('4. Borrar contraseña.')
    print('5. Generar contraseña aleatoriamente')
    print('6. Salir')
    opcion = input('Elige tu opción: ')

    #Verificamos que se haya escogido la opción correcta
    if opcion == 0 or opcion > 6:
        clear()
        print('Escoge una opción valida... -.-')
        sleep(5)
        clear()
        menu()
    else:
        return opcion #Si todo está bien, permite usar la opcion para escoger la siguiente pantalla