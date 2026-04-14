import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
    
    def registrar(self, usuario_data):
        #Encripta contraseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.contraseña.encode('utf-9'),salt)
        
        conn = self.db.get_connetion()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, contraseña) VALUES (%s, %s, %s)"
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def validar_login(self, email, contraseña):
        conn = self.db.get_connetion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
        user = cursor.fetchone()
        conn.close
        
        if user and bcrypt.checkpw(contraseña.encode('utf-8'), user['contraseña'].encode('utf-8')):
            return user
        return None