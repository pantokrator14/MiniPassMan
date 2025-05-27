import bcrypt
import random
from string import ascii_letters, digits, punctuation

class PasswordManager:
    def __init__(self, longitud_min: int = 12):
        self.caracteres = ascii_letters + digits + punctuation
        self.longitud_min = longitud_min
        
    def generar(self) -> str:
        while True:
            try:
                longitud = int(input(f"Longitud (mín {self.longitud_min}): "))
                if longitud < self.longitud_min:
                    raise ValueError
                break
            except ValueError:
                print(f"❌ Mínimo {self.longitud_min} caracteres")
                
        return ''.join(random.choices(self.caracteres, k=longitud))

    def encriptar(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verificar(self, password: str, hash: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hash)