import bcrypt
from .database import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()