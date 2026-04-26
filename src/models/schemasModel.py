from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuarioShema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    descripcion: Optional[str] = None
    fecha_limite: Optional[date] = None
    hora_limite: Optional[time] = None
    prioridad: Optional[str] = "media"
    clasificacion: Optional[str] = "personal"