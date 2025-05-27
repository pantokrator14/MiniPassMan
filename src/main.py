# Archivo: main.py (actualizado)
from func import conectar, menu
import text2art
import pymongo.errors

presentacion = text2art.text2art('MINIPASSMAN', font='cybermedium')
creador = text2art.text2art('By: Julio José Adam Martínez', font='white_bubble')

print(presentacion)
print(creador)
print('-' * 80)

def obtener_credenciales():
    while True:
        try:
            usuario = input('Ingrese su usuario: ')
            password = input('Ingrese su contraseña: ')
            return usuario, password
        except KeyboardInterrupt:
            print("\n\n❌ Operación cancelada por el usuario")
            exit()

def main():
    usuario, password = obtener_credenciales()
    
    # Intento de conexión con manejo de errores
    try:
        coleccion = conectar(usuario, password)
        print("\n✅ Conexión exitosa a la base de datos!")
        menu(coleccion)
    except pymongo.errors.ConnectionFailure:
        print("\n❌ Error de conexión: Verifique su conexión a Internet")
    except pymongo.errors.OperationFailure:
        print("\n🔒 Error de autenticación: Usuario o contraseña incorrectos")
    except Exception as e:
        print(f"\n⚠️ Error inesperado: {str(e)}")
    finally:
        print("\nGracias por usar MiniPassMan!")

if __name__ == "__main__":
    main()