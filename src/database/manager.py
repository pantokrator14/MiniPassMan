import pymongo
from pymongo import errors
from getpass import getpass
from tabulate import tabulate
import pyperclip

class DatabaseManager:
    def __init__(self, usuario: str, password: str):
        self.url = f"mongodb+srv://{usuario}:{password}@minipassman.ouhpb.mongodb.net/"
        self.client = None
        self.collection = None
        
    def connect(self):
        try:
            self.client = pymongo.MongoClient(
                self.url,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=30000
            )
            self.client.server_info()
            db = self.client['MiniPassMan']
            self.collection = db['passwords']
            return True
        except errors.ServerSelectionTimeoutError:
            raise ConnectionError("Error de conexión")
        except errors.OperationFailure:
            raise AuthenticationError("Credenciales inválidas")
        except Exception as e:
            raise Exception(f"Error: {str(e)}")

    def crear_registro(self, password_encriptada: bytes):
        documento = {
            "website": input("Sitio web: "),
            "username": input("Usuario: "),
            "password": password_encriptada,
            "descripcion": input("Descripción: ")
        }
        
        result = self.collection.insert_one(documento)
        print(f"✅ Registro creado (ID: {result.inserted_id})")

    def mostrar_registros(self, filtro: dict = None):
        try:
            resultados = list(self.collection.find(filtro, {'_id': 0}))
            if not resultados:
                print("❌ No hay registros")
                return
                
            headers = resultados[0].keys()
            rows = [r.values() for r in resultados]
            print(tabulate(rows, headers=headers))
        except errors.PyMongoError:
            print("❌ Error al leer registros")

    def editar_registro(self):
        sitio = input("Sitio web a modificar: ")
        usuario = input("Usuario a modificar: ")
        
        nuevos_valores = {
            "website": input("Nuevo sitio web (Enter para mantener): ") or None,
            "username": input("Nuevo usuario (Enter para mantener): ") or None,
            "password": getpass("Nueva contraseña (Enter para mantener): ") or None,
            "descripcion": input("Nueva descripción (Enter para mantener): ") or None
        }
        
        actualizacion = {k: v for k, v in nuevos_valores.items() if v is not None}
        if not actualizacion:
            print("ℹ️ No se realizaron cambios")
            return
            
        result = self.collection.update_one(
            {"website": sitio, "username": usuario},
            {"$set": actualizacion}
        )
        print(f"✅ {result.modified_count} registro(s) actualizado(s)")

    def borrar_registro(self):
        sitio = input("Sitio web a borrar: ")
        usuario = input("Usuario a borrar: ")
        
        confirmar = input("¿Confirmar borrado? (s/n): ").lower()
        if confirmar != 's':
            return
            
        result = self.collection.delete_one({"website": sitio, "username": usuario})
        print(f"✅ {result.deleted_count} registro(s) eliminado(s)")

    def copiar_contraseña(self):
        usuario = input("Usuario: ")
        registro = self.collection.find_one({"username": usuario}, {'_id': 0})
        
        if registro:
            pyperclip.copy(registro['password'].decode())
            print("📋 Contraseña copiada al portapapeles")
        else:
            print("❌ Usuario no encontrado")