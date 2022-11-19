import pewee

from datetime import datetime
from enum import unique

from v1.utils.database import db

from v1.model.docente import Docente

class Curso(pewee.Model):
    id_curso: pewee.Charfield(unique=True,index=True)
    curso: pewee.Charfield(unique=True,index=True)
    descripcion: pewee.TextField()
    costo: pewee.IntegerField()
    id_docente: pewee.ForeignKeyField(Docente, backref="dream_team_education")
    docente: pewee.Charfield(unique=True,index=True)
    sesiones: pewee.IntegerField()
    duracion_sesion: pewee.IntegerField()
    fecha_creacion: datetime =  pewee.DateTimeField( default=datetime.now())
    
    class Meta:
        database = db


