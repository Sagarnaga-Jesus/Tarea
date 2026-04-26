from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioShema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_Usuario(self, nombre, email, contraseña):
        try:
            nuevo_usuario = UsuarioShema(
                nombre=nombre,
                email=email,
                password=contraseña
            )

            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"

        except ValidationError as e:
            return False, e.errors()[0]['msg']
    
    def login(self, email, password):
        try:
            print("ENTRÉ AL LOGIN CONTROLLER")
    
            user = self.model.validar_login(email, password)
    
            if user:
                return user, "Login correcto"
            else:
                return False, "Credenciales incorrectas"
    
        except ValidationError as e:
            return False, e.errors()[0]['msg']