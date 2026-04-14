from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioShema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_Usuario(self, nombre, email, contraseña):
        try:
            #Vlidr datos con el shema
            nuevo_usuario = UsuarioShema(nombre=nombre, email=email, contraseña=contraseña)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            # Retorn el primer error de validacion encotrado
            
            return False, e.errors()[0],{'msg'}