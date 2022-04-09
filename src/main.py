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
if opcion == 1:
    crear(coleccion)
elif opcion == 2:
    consultar(coleccion)
elif opcion == 3:
    editar(coleccion)
elif opcion == 4:
    borrar(coleccion)
elif opcion == 5:
    generator()
elif opcion == 6:
    print('Saliendo del programa...')
    exit(5)
