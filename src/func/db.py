from asyncio.windows_events import NULL
from nturl2path import url2pathname
from ssl import _PasswordType
import pymongo as pym

url = "mongodb+srv://{usuario}:{password}@minipassman.ouhpb.mongodb.net/"
client = pym.MongoClient(url)
db = client.MiniPassMan
collection = db['passwords']

#---------------------------------------------------------

#          F   U   N   C   T   I   O   N   S

#---------------------------------------------------------

def crear():    #Crear contraseñas
    opcion = input("1.Colocar mi propia contraseña \n2.Generar contraseña aleatoria automáticamente")
    if opcion == 1:
        sitio = input("Nombre del sitio web: ")
        usuario = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        nota = input("Ingrese una nota o descripción: ")
        collection.insert_one({"website":sitio, "username":usuario, "password":contraseña, "descripcion":nota})
    elif opcion == 2:
        print("Espere mientras creamos su contraseña...")
    else:
        print("ingrese una opción valida... -.-")
        crear()

def buscar():
    nombre = input("¿Como se llama el sitio web que busca? ")
    resultado = collection.find({"website": nombre})
    if resultado == NULL: #Posible fuente de errores, cambiar de ser necesario
        print("Sitio web no encontrado... Intente nuevamente.")
        buscar()
    else:
        for res in resultado:
            print(res['username', 'password', 'descripcion'])

def borrar():
    nombre = input("¿Como se llama el sitio web que busca? ")
    usuario = input("")
    resultado = collection.delete_one({"website": nombre})

