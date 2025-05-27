# 🔒 MiniPassMan - Gestor de Contraseñas Seguro

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green)
![Licencia](https://img.shields.io/badge/Licencia-MIT-orange)

Gestor de contraseñas en consola con encriptación BCrypt y almacenamiento seguro en MongoDB. Desarrollado en Python.

## 🌟 Características Principales

- 🔐 Encriptación avanzada con BCrypt
- 🌐 Almacenamiento en MongoDB Atlas (nube)
- 🛠 Generador de contraseñas robustas
- 📋 Integración con portapapeles
- 📂 Gestión CRUD completa
- 🖥 Interfaz intuitiva con ASCII art

## 🚀 Instalación

1. **Clonar repositorio**:
```bash
git clone https://github.com/tu-usuario/MiniPassMan.git
cd MiniPassMan

2. **Instalar dependencias**:

```bash
pip install -r requirements.txt

3. **Configurar MongoDB Atlas**:

    Crear cluster gratuito en MongoDB Atlas

    Reemplazar URL de conexión en database/manager.py (línea 12)

## 🖥 Uso
```bash
python src/main.py

## Flujo de trabajo:

    Ingresar credenciales de MongoDB Atlas

    Navegar por el menú interactivo:

    [1] Nueva contraseña
    [2] Ver registros
    [3] Editar
    [4] Borrar
    [5] Generar Password
    [6] Salir

## 🗂 Estructura del Proyecto

/MiniPassMan
├── src/
│   ├── main.py
│   ├── database/       # Gestión MongoDB
│   ├── security/       # Encriptación y generación
│   └── interface/      # Lógica de interfaz
├── requirements.txt
└── README.md

## 🛠 Tecnologías Utilizadas

    Python 3.9+

    MongoDB Atlas - Base de datos en la nube

    BCrypt - Encriptación de contraseñas

    PyMongo - Driver MongoDB para Python

    Tabulate - Visualización de datos en tablas

    Text2Art - Interfaz con ASCII art

## 🔧 Requisitos Mínimos

    Python 3.9 o superior

    Cuenta en MongoDB Atlas

    100 MB de espacio libre

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Sigue estos pasos:

    Haz un fork del proyecto

    Crea tu rama (git checkout -b feature/nueva-funcionalidad)

    Haz commit de tus cambios (git commit -m 'Agrega nueva funcionalidad')

    Haz push a la rama (git push origin feature/nueva-funcionalidad)

    Abre un Pull Request


📧 Contacto

Julio José Adam Martínez
📩 julioblogs1998@gmail.com
