import text2art
from os import system, name
from time import sleep
from security.passwords import PasswordManager

class MenuManager:
    def __init__(self, db_manager):
        self.db = db_manager
        self.pw_manager = PasswordManager()
        
    def clear(self):
        system('cls' if name == 'nt' else 'clear')
        
    def mostrar_menu_principal(self):
        while True:
            self.clear()
            print(text2art.text2art("MiniPassMan", font="block"))
            print("[1] Nueva contraseña\n[2] Ver registros\n[3] Editar\n[4] Borrar\n[5] Generar Password\n[6] Salir")
            
            opcion = input("\nOpción: ")
            self.procesar_opcion(opcion)
            
    def procesar_opcion(self, opcion: str):
        match opcion:
            case '1': self._crear_registro()
            case '2': self._mostrar_registros()
            case '3': self._editar_registro()
            case '4': self._borrar_registro()
            case '5': self._generar_password()
            case '6': self._salir()
            case _: print("❌ Opción inválida")

    def _crear_registro(self):
        try:
            password = getpass("Contraseña: ")
            hash = self.pw_manager.encriptar(password)
            self.db.crear_registro(hash)
            input("\n✅ Registro creado. Enter para continuar...")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

    def _mostrar_registros(self):
        self.db.mostrar_registros()
        input("\nPresione Enter para continuar...")

    def _editar_registro(self):
        self.db.editar_registro()
        input("\nPresione Enter para continuar...")

    def _borrar_registro(self):
        self.db.borrar_registro()
        input("\nPresione Enter para continuar...")

    def _generar_password(self):
        password = self.pw_manager.generar()
        pyperclip.copy(password)
        print(f"\n🔑 Nueva contraseña: {password}")
        input("📋 Copiada al portapapeles. Enter para continuar...")

    def _salir(self):
        print("\n🔒 Saliendo del sistema...")
        sleep(1)
        exit()