from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioShema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_Usuario(self, nombre, email, contraseña):
        try:
            #Validar datos con el shema
            nuevo_usuario = UsuarioShema(nombre=nombre, email=email, contraseña=contraseña)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            # Retorn el primer error de validacion encotrado
            
            return False, e.errors()[0],{'msg'}
    
    def login(self, email, password):
        try:
            #Validar datos con shemas
            usuario_login = UsuarioShema(email=email, contraseña=password)
            success = self.model.iniciar_sesion(usuario_login)
            if success:
                return True
            else:
                return False,"Credenciales incorrectas"
            
        except ValidationError as e:
            #Retornar el primer error de la validacion encontrada
            return False, e.error()[0]['msg']