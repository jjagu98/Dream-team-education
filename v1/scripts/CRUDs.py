from re import S
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid


app = FastAPI()

cursos = []
usuarios = []
docentes = []

# Post model
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

class Usuario(BaseModel):
    id: str
    nomrbre: str
    email: str
    carrito: list
    fecha_creacion: datetime =  datetime.now()

class Docente(BaseModel):
    id: str
    nombre: str
    email: str
    especialidad: str
    fecha_creacion: datetime =  datetime.now()

@app.get('/')
def read_root():
    return {"Welcome": "Bienvenidos a Dream Team Education"}

@app.get('/cursos')
def get_cursos():
    return cursos

# Create
@app.post('/cursos')
def save_curso(curso: Curso):
    curso.id_curso = str(uuid())
    curso.id_docente = str(uuid())
    cursos.append(curso.dict())
    return cursos[-1]

# Read
@app.get('/cursos/{id_curso}')
def get_curso(id_curso: str):
    for curso in cursos:
        if curso["id_curso"] == id_curso:
            return curso
    raise HTTPException(status_code=404, detail="Curso no encontrado")

# Update
@app.put('/cursos/{id_curso}')
def update_curso(id_curso: str, updatedCurso: Curso):
    for index, curso in enumerate(cursos):
        if curso["id_curso"] == id_curso:
            cursos[index]["curso"]= updatedCurso.dict()["curso"]
            cursos[index]["descripcion"]= updatedCurso.dict()["descripcion"]
            cursos[index]["costo"]= updatedCurso.dict()["costo"]
            cursos[index]["id_docente"]= updatedCurso.dict()["id_docente"]
            cursos[index]["docente"]= updatedCurso.dict()["docente"]
            cursos[index]["sesiones"]= updatedCurso.dict()["sesiones"]
            cursos[index]["duracion_sesion"]    = updatedCurso.dict()["duracion_sesion"]
            cursos[index]["calificacion"]= updatedCurso.dict()["calificacion"]
            return {"message": "El curso ha sido actualizado satisfactoriamente"}
    raise HTTPException(status_code=404, detail="Curso no encontrado")

# Delete
@app.delete('/cursos/{id_curso}')
def delete_curso(id_curso: str):
    for index, curso in enumerate(cursos):
        if curso["id_curso"] == id_curso:
            cursos.pop(index)
            return {"message": "El curso ha sido eliminado satisfactoriamente"}
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@app.get('/usuarios')
def get_usuarios():
    return usuarios

# Create
@app.post('/usuarios')
def save_usuario(usuario: Usuario):
    usuario.id = str(uuid())
    usuario.carrito = []
    usuarios.append(usuario.dict())
    return usuarios[-1]

# Read
@app.get('/usuarios/{id}')
def get_usuario(id: str):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Update
@app.put('/usuarios/{id}')
def update_usuario(id: str, updatedUsuario: Usuario):
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuarios[index]["nombre"]= updatedUsuario.dict()["nombre"]
            usuarios[index]["email"]= updatedUsuario.dict()["email"]
            return {"message": "El usuario se ha actualizado satisfactoriamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Delete
@app.delete('/usuarios/{id}')
def delete_usuario(id: str):
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuarios.pop(index)
            return {"message": "El usuario ha sido eliminado de manera satisfactoria"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.get('/docentes')
def get_docentes():
    return docentes

# Create
@app.post('/docentes')
def save_docente(docente: Docente):
    docente.id = str(uuid())
    docentes.append(docente.dict())
    return docentes[-1]

# Read
@app.get('/docentes/{id}')
def get_docente(id: str):
    for docente in docentes:
        if docente["id"] == id:
            return docente
    raise HTTPException(status_code=404, detail="Docente no encontrado")

# Update
@app.put('/docentes/{id}')
def update_docente(id: str, updatedDocente: Docente):
    for index, docente in enumerate(docentes):
        if docente["id"] == id:
            docentes[index]["nombre"] = updatedDocente.dict()["nombre"]
            docentes[index]["email"] = updatedDocente.dict()["email"]
            docentes[index]["especialidad"] = updatedDocente.dict()["especialidad"]
            return {"message": "El docente se ha actualizado satisfactoriamente"}
    raise HTTPException(status_code=404, detail="Docente no encontrado")

# Delete
@app.delete('/docentes/{id}')
def delete_docente(id: str):
    for index, docente in enumerate(docentes):
        if docente["id"] == id:
            docentes.pop(index)
            return {"message": "El docente ha sido eliminado de manera satisfactoria"}
    raise HTTPException(status_code=404, detail="Docente no encontrado")

#Filtro de cursos
@app.get('/{calificacion}')
def filtro_cursos(calificacion: float):
    lf = []
    for curso in cursos:
        if curso["calificacion"] >= calificacion:
            lf.append(curso)
    return lf

#Carrito
@app.get('/usuarios/{id}/carrito')
def carrito(id: str, id_curso: str):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["carrito"].append(id_curso)
            return usuario["carrito"]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#Factura
@app.get('/usuario/{id}/factura')
def factura(id: str):
    total=0
    for usuario in usuarios:
        if usuario["id"] == id:
            for idcurso in usuario["carrito"]:
                for curso in cursos:
                    if curso["id_curso"] == idcurso:
                        total=curso["costo"]+total
            usuario["carrito"].append(total)
            return usuario["carrito"]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")    

#Porcentaje profesores
