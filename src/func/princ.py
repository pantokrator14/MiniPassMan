from db import crear, consultar, editar, borrar, copiar
from gen import generator
import pyperclip
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
def menu(coleccion):
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
        menu()
    else:
        if opcion == 1:
            clear()
            crear(coleccion)
            print("Regresando al menu...")
            sleep(5)
            menu()
        elif opcion == 2:
            consultar(coleccion)
            opcion = input("Qué desea hacer ahora?\n1.Volver al menú\n2.Copiar password")
            if opcion == 1:
                print("Volviendo al menú...")
                sleep(5)
                menu()
            elif opcion == 2:
                copiar(coleccion)
                print("Regresando al menu...")
                sleep(5)
                menu()
            else:
                print("Opción inválida... Regresando al menú principal")
                menu()
        elif opcion == 3:
            editar(coleccion)
            print("Regresando al menu...")
            sleep(5)
            menu()
        elif opcion == 4:
            borrar(coleccion)
            print("Regresando al menu...")
            sleep(5)
            menu()
        elif opcion == 5:
            password = generator()
            pyperclip.copy(password)
            print('Password copiado en el portapapeles.')
            print("Regresando al menu...")
            sleep(5)
            menu()
        elif opcion == 6:
            print('Saliendo del programa...')
            exit(5) #Si todo está bien, permite usar la opcion para escoger la siguiente pantalla