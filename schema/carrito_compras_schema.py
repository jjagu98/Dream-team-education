from re import S
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid


class Carrito_compra(BaseModel):
    id_compra:int
    id_usuario:str
    id_curso:int

