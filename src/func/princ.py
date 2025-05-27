from db import crear, consultar, editar, borrar, copiar
from gen import generator
import pyperclip
import text2art
from os import system, name 
from time import sleep

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def menu(coleccion):
    while True:  # Bucle principal en lugar de recursión
        clear()
        logo = text2art.text2art("MENU", font="block")
        print(logo)
        print('-' * 80)
        print('1. Guardar nueva contraseña')
        print('2. Mostrar contraseñas')
        print('3. Modificar datos')
        print('4. Borrar contraseña')
        print('5. Generar contraseña aleatoria')
        print('6. Salir\n')

        try:  # Manejo de errores para entrada no numérica
            opcion = int(input('Elige tu opción (1-6): '))
        except ValueError:
            input('\n❌ Entrada inválida. Presiona Enter para continuar...')
            continue

        if opcion == 1:
            clear()
            crear(coleccion)
            input('\n✅ Contraseña guardada. Presiona Enter para continuar...')

        elif opcion == 2:
            clear()
            consultar(coleccion)
            sub_opcion = input('\n1. Volver al menú\n2. Copiar contraseña\nOpción: ')
            
            if sub_opcion == '2':
                copiar(coleccion)
                input('\n📋 Contraseña copiada. Presiona Enter para continuar...')
        
        elif opcion == 3:
            clear()
            editar(coleccion)
            input('\n✅ Datos modificados. Presiona Enter para continuar...')

        elif opcion == 4:
            clear()
            borrar(coleccion)
            input('\n✅ Contraseña eliminada. Presiona Enter para continuar...')

        elif opcion == 5:
            clear()
            password = generator()
            pyperclip.copy(password)
            print(f'\n🔑 Contraseña generada: {password}')
            input('📋 Copiada al portapapeles. Presiona Enter para continuar...')

        elif opcion == 6:
            clear()
            print(text2art.text2art("Adios!", font="cybermedium"))
            sleep(1)
            break  # Salir del bucle

        else:  # Manejo de opciones fuera de rango
            input('\n❌ Opción no válida. Presiona Enter para continuar...')