from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioShema(BaseModel):
    nombre: str = Field(min_length=8, max_length=100)
    email: EmailStr
    password: str = Field(min_legth=8)
    
class TareaShema(BaseModel):
    titulo: str = Field(nim_legth=1, max_legth=200)
    description: Optional[str] = None
    prioridad: str = "media"
    clasificacion: str = "personal"