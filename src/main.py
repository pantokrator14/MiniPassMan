from database.manager import DatabaseManager
from interface.menu import MenuManager

def main():
    try:
        print("=== Bienvenido ===")
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        
        db_manager = DatabaseManager(usuario, password)
        if db_manager.connect():
            MenuManager(db_manager).mostrar_menu_principal()
            
    except ConnectionError as e:
        print(f"\n❌ {str(e)}")
    except Exception as e:
        print(f"\n⚠️ Error crítico: {str(e)}")
    finally:
        print("\nGracias por usar MiniPassMan!")

if __name__ == "__main__":
    main()