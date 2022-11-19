import pewee
from enum import unique
from datetime import datetime

from v1.utils.database import db


class Usuario(pewee.Model):
    id: pewee.Charfield(unique=True,index=True)
    nomrbre: pewee.Charfield(unique=True,index=True)
    email: pewee.Charfield(unique=True,index=True)
    fecha_creacion: datetime = pewee.DateTimeField( default=datetime.now())
    
    class Meta:
        database = db