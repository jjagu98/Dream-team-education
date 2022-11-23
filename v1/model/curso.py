import peewee

from datetime import datetime
from enum import unique

from v1.utils.database import db

from v1.model.docente import Docente

class Curso(peewee.Model):
    id_curso: peewee.Charfield(unique=True,index=True)
    curso: peewee.Charfield(unique=True,index=True)
    descripcion: peewee.TextField()
    costo: peewee.IntegerField()
    id_docente: peewee.ForeignKeyField(Docente, backref="dream_team_education")
    docente: peewee.Charfield(unique=True,index=True)
    sesiones: peewee.IntegerField()
    duracion_sesion: peewee.IntegerField()
    fecha_creacion: datetime =  peewee.DateTimeField( default=datetime.now())
    
    class Meta:
        database = db


