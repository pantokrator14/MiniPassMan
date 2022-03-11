from ssl import _PasswordType
import pymongo as pym

client = pym.MongoClient("mongodb+srv://minipassman-admin:password@minipassman.ouhpb.mongodb.net/name?retryWrites=true&w=majority")
db = client.MiniPassMan
collection = db['passwords']

#---------------------------------------------------------

#          F   U   N   C   T   I   O   N   S

#---------------------------------------------------------

def crear():    #Crear contraseñas
    opcion = input("1.Colocar mi propia contraseña \n2.Generar contraseña aleatoria automáticamente")
    if opcion == 1:
        usuario = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        nota = input("Ingrese una nota o descripción: ")
        collection.insert_one({"username":usuario, "password":contraseña, "descripcion":nota})
    elif opcion == 2:
        print("Espere mientras creamos su contraseña...")
    else:
        print("ingrese una opción valida... -.-")
        crear()

