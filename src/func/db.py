from nturl2path import url2pathname
from ssl import _PasswordType
import pymongo as pym
import tabulate
import pyperclip
from gen import salt, check

def conectar(usuario, password):
    url = f"mongodb+srv://{usuario}:{password}@minipassman.ouhpb.mongodb.net/" #La F permite usar las variables dentro de las cadenas de texto, por lo visto. Investigar...
    client = pym.MongoClient(url)
    db = client.MiniPassMan
    collection = db['passwords']
    return collection

#---------------------------------------------------------

#          F   U   N   C   T   I   O   N   S

#---------------------------------------------------------

def crear(collection):    #Crear contraseñas
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
        crear(collection) #Confirmar si al hacer esto no pide de nuevo la variable collection, creo que saldra un error...

def consultar(collection):
    opcion = int(input('Desea:\n1.Mostrar todas las contrasenas\n2.Buscar por sitio web'))
    if opcion == 1:
        resultados = collection.find()
        print(tabulate(resultados))
    elif opcion ==2:
        nombre = input("¿Como se llama el sitio web que busca? ")
        resultado = collection.find({"website": nombre})
        if resultado == False: #Posible fuente de errores, cambiar de ser necesario
            print("Sitio web no encontrado... Intente nuevamente.")
            consultar(collection)
        else:
            for res in resultado:
                print(tabulate(res))

def borrar(collection):
    nombre = input("¿Como se llama el sitio web que busca? ")
    usuario = input("")
    resultado = collection.delete_one({"website": nombre})

