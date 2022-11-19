from v1.model.usuario import Usuario
from v1.model.docente import Docente
from v1.model.curso import Curso

from v1.utils.database import db

def create_tables():
    with db:
        db.create_tables([Usuario,Docente,Curso])
        