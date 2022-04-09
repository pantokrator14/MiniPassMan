import pyperclip
from func import conectar, crear, consultar, copiar, editar, borrar, menu, clear, generator
import text2art

presentacion = text2art('MINIPASSMAN', font='cybermedum')
creador = text2art('By: Julio José Adam Martínez', font='white_bubble')

print(presentacion)
print(creador)
print('---------------------------------------------------------------------------------------------')

usuario = input('Ingrese su usuario: ')
password = input('Ingrese su contraseña: ')

coleccion = conectar(usuario, password)

opcion = menu()
print('---------------------------------------------------------------------------------------------')
if opcion == 1:
    crear(coleccion)
elif opcion == 2:
    consultar(coleccion)
    opcion = input("Qué desea hacer ahora?\n1.Volver al menú\n2.Copiar password")
    if opcion == 1:
        menu()
    elif opcion == 2:
        copiar(coleccion)
    else:
        print("Opción inválida... Regresando al menú principal")
        menu()
elif opcion == 3:
    editar(coleccion)
elif opcion == 4:
    borrar(coleccion)
elif opcion == 5:
    password = generator()
    pyperclip.copy(password)
    print('Password copiado en el portapapeles.')
elif opcion == 6:
    print('Saliendo del programa...')
    exit(5)
