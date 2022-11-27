from re import S
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid


class Usuario(BaseModel):
    """
    Esta clase crea la estructura para instanciar objetos de tipo Usuario
    """
    id: str
    nombre: str
    fecha_creacion: datetime =  datetime.now()
    email: str
    