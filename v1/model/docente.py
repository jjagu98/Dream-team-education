import peewee
from enum import unique
from datetime import datetime
from v1.utils.database import db


class Docente(peewee.Model):
    id: peewee.Charfield(unique=True,index=True)
    nombre: peewee.Charfield(unique=True,index=True)
    email: peewee.Charfield(unique=True,index=True)
    especialidad: peewee.Charfield(unique=True,index=True)
    fecha_creacion: datetime =  peewee.DateTimeField( default=datetime.now())
    
    class Meta:
        database = db