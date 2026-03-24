from src.models.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_Usuario(self, nombre, email, contraseña):
        try:
            #Vlidr datos con el shema
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, contraseña=contraseña)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario crado correctamente"
        except ValidationError as e:
            # Retorn el primer error de validacion encotrado
            
            return False, e.errors()[0],{'msg'}