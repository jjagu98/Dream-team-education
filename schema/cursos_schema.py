from re import S
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid



class Curso(BaseModel):
    id_curso: str
    curso: str
    descripcion: Text
    costo: int
    id_docente: str
    docente: str
    sesiones: int
    duracion_sesion: int
    calificacion: float
    fecha_creacion: datetime =  datetime.now()





