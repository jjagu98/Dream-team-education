from re import S
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text
from datetime import datetime
from uuid import uuid4 as uuid
from model.conexion_usuario import Conexionusuario
from model.conexion_docentes import Conexiondocente
from model.conexion_cursos import Conexioncursos
from model.conexion_carrito_compras import Conexioncarrito

from schema.usuario_schema import Usuario
from schema.docente_schema import Docente
from schema.cursos_schema import Curso
from schema.carrito_compras_schema import Carrito_compra

app = FastAPI()
conn_usuario=Conexionusuario()
conn_docente=Conexiondocente()
conn_curso=Conexioncursos()
conn_carrito=Conexioncarrito()


@app.get('/')
def read_root():
    conn_usuario
    conn_docente
    conn_curso
    return {"Welcome": "Bienvenidos a Dream Team Education"}

@app.post('/usuarios')
def save_usuario(usuario: Usuario):
     data=usuario.dict()
     conn_usuario.write(data)

@app.get('/usuarios')
def get_usuarios():
    return conn_usuario.read_all()

@app.get('/usuarios/{id}')
def get_usuario(id: str):
    return conn_usuario.get_usuario(id)  

@app.delete('/usuarios/{id}')
def delete_usuario(id: str):
    conn_usuario.delete_usuario(id)
    return {"message": "El usuario ha sido eliminado satisfactoriamente"}

@app.put('/usuarios/{id}')
def update_usuario(updatedUsuario: Usuario):
   conn_usuario.update_usuario(updatedUsuario)
   return {"message": "El usuario se ha actualizado satisfactoriamente"}

@app.post('/docente')
def save_docente(docente: Docente):
     data=docente.dict()
     conn_docente.write(data)

@app.get('/docente')
def get_docentes():
    return conn_docente.read_all()

@app.get('/docente/{id}')
def get_docente(id: str):
    return conn_docente.get_docente(id)

@app.delete('/docente/{id}')
def delete_docente(id: str):
    conn_docente.delete_docente(id)
    return {"message": "El docente ha sido eliminado satisfactoriamente"}

@app.put('/docente/{id}')
def update_docente(updatedDocente: Docente):
   conn_usuario.update_usuario(updatedDocente)
   return {"message": "El docente se ha actualizado satisfactoriamente"}


@app.post('/curso')
def save_curso(curso: Curso):
     data=curso.dict()
     conn_curso.write(data)

@app.get('/cursos')
def get_cursos():
    return conn_curso.read_all()

@app.get('/cursos/{id}')
def get_curso(id: str):
    return conn_curso.get_curso(id)
    
@app.delete('/cursos/{id}')
def delete_curso(id: str):
    conn_curso.delete_curso(id)        
    return {"message": "El curso ha sido eliminado satisfactoriamente"}
    
@app.put('/cursos/{id}')
def update_curso(updatedCurso: Curso):
   conn_usuario.update_usuario(updatedCurso)
   return {"message": "El curso se ha actualizado satisfactoriamente"}

@app.post('/carritocompras')
def save_compra(carrito:Carrito_compra ):
     data=carrito.dict()
     conn_usuario.write(data)

@app.get('/carritocompras/{id}')
def get_total(id: str):
    return conn_carrito.factura_total(id)
