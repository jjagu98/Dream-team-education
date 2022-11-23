import peewee
from enum import unique
from datetime import datetime

from v1.utils.database import db


class Usuario(peewee.Model):
    id: peewee.Charfield(unique=True,index=True)
    nomrbre: peewee.Charfield(unique=True,index=True)
    email: peewee.Charfield(unique=True,index=True)
    fecha_creacion: datetime = peewee.DateTimeField( default=datetime.now())
    
    class Meta:
        database = db