from nturl2path import url2pathname
from ssl import _PasswordType
import pymongo as pym
import tabulate
import pyperclip
from getpass import getpass
from gen import generator


#Change the url based on your own mongoDB database, its the only thing you have to change.
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
        print('Datos guardados bajo el ID: ',respuesta.inserted_id)

    else:
        print("ingrese una opción valida... -.-")
        crear(collection) #Confirmar si al hacer esto no pide de nuevo la variable collection, creo que saldra un error...

def consultar(collection):
    opcion = int(input('Desea:\n1.Mostrar todas las contrasenas\n2.Buscar por sitio web'))
    if opcion == 1:
        resultados = collection.find(projection={'_id':False}) #Se presume que esto recogera todos los campos de  las contrasenas exceptuando el id
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

