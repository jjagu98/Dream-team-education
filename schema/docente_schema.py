from re import S
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid

class Docente(BaseModel):
    id: str
    nombre: str
    email: str
    especialidad: str
    fecha_creacion: datetime =  datetime.now()