from func import conectar, menu
import text2art

presentacion = text2art('MINIPASSMAN', font='cybermedum')
creador = text2art('By: Julio José Adam Martínez', font='white_bubble')

print(presentacion)
print(creador)
print('---------------------------------------------------------------------------------------------')

usuario = input('Ingrese su usuario: ')
password = input('Ingrese su contraseña: ')

coleccion = conectar(usuario, password)

menu(coleccion)
