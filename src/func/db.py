from nturl2path import url2pathname
from ssl import _PasswordType
import pymongo as pym
import tabulate
import pyperclip
from getpass import getpass
from gen import generator


#Change the url based on your own mongoDB database, its the only thing you have to change.
def conectar(usuario, password):
    url = f"mongodb+srv://{usuario}:{password}@minipassman.ouhpb.mongodb.net/" # F seems to allow us to use variables on a chain.
    client = pym.MongoClient(url)
    db = client.MiniPassMan
    collection = db['passwords']
    return collection

#---------------------------------------------------------

#          F   U   N   C   T   I   O   N   S

#---------------------------------------------------------

def crear(collection):    #Create data
    opcion = input("1.Colocar mi propia contraseña \n2.Generar contraseña aleatoria automáticamente")
    if opcion == 1:
        sitio = input("Nombre del sitio web: ")
        usuario = input("Ingrese nombre de usuario: ")
        contraseña = getpass("Ingrese la contraseña: ")
        nota = input("Ingrese una nota o descripción: ")
        respuesta = collection.insert_one({"website":sitio, "username":usuario, "password":contraseña, "descripcion":nota})
        print('Datos guardados bajo el ID: ',respuesta.inserted_id)
    elif opcion == 2:
        print("Espere mientras creamos su contraseña...")
        password = generator()
        print("Contraseña creada..")
        sitio = input("Nombre del sitio web: ")
        usuario = input("Ingrese nombre de usuario: ")
        nota = input("Ingrese una nota o descripción: ")
        respuesta = collection.insert_one({"website":sitio, "username":usuario, "password":password, "descripcion":nota})
        
        if respuesta.acknowledged:
            print('Datos guardados bajo el ID: ',respuesta.inserted_id)

    else:
        print("ingrese una opción valida... -.-")
        crear(collection)

def consultar(collection):
    opcion = int(input('Desea:\n1.Mostrar todas las contrasenas\n2.Buscar por sitio web'))
    if opcion == 1:
        resultados = collection.find(projection={'_id':False}) #It seems to return all the values of the document except for the ID
        for res in resultados:
            print(tabulate(res))
    elif opcion ==2:
        nombre = input("¿Como se llama el sitio web que busca? ")
        resultado = collection.find({"website": nombre})
        if resultado.acknowledged: #Possible bug, change if necessary
            for res in resultado:
                print(tabulate(res))
        else:
            print("Sitio web no encontrado... Intente nuevamente.")
            consultar(collection)

def copiar(collection):
    nombre = input('nombre de usuario: ')
    filtro = {'username':nombre}
    password = collection.find_one(filtro)['password']
    pyperclip.copy(password)
    print(f'Password de {nombre} guardado en el portapales!')

def editar(collection):

    nombre = input('nombre: ')
    filtro = {'name':nombre}
    newName = input("Nuevo nombre de usuario: ")
    sitio = input('Nuevo enlace: ')
    password = getpass('NUEVO password: ')
    description = input("Nueva descripción: ")
    valores = {'$set':{'password':password,'website':sitio,'username':newName, 'descripcion': description}}
    respuesta = collection.update_one(filtro,valores)

    if respuesta.acknowledged:
        print('Datos modificados!')


def borrar(collection):
    nombre = input("¿Como se llama el sitio web que busca? ")
    usuario = input("Ingrese el nombre de usuario respectivo: ")
    resultado = collection.delete_one({"website": nombre, "username": usuario})

    if resultado.acknowledged:
        print("Datos borrados con éxito!")
    else:
        print("ERROR. Data no encontrada.")

