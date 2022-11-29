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
conn_usuario = Conexionusuario()
conn_docente = Conexiondocente()
conn_curso = Conexioncursos()
conn_carrito = Conexioncarrito()


@app.get('/')
def read_root() -> dict:
    """
    Raíz principal de la plataforma educativa.

    Returns:
        dict: Mensaje de bienvenida de la página principal.
    """
    conn_usuario
    conn_docente
    conn_curso
    return {"Welcome": "Bienvenidos a Dream Team Education"}

@app.post('/usuarios')
def save_usuario(usuario: Usuario) -> None:
    """
    Crea el usuario en la tabla usuarios.

    Args:
        usuario (Usuario): Datos del usuario.
    """
    data=usuario.dict()
    conn_usuario.write(data)

@app.get('/usuarios')
def get_usuarios() -> list:
    """
    Muestra todos los usuarios registrados.

    Returns:
        list: Lista que contiene todos los usuarios registrados.
    """
    return conn_usuario.read_all()

@app.get('/usuarios/{id}')
def get_usuario(id: str) -> tuple:
    """
    Muestra los datos del usuario, si existe.

    Args:
        id (str): id del usuario que se desea buscar.

    Returns:
        tuple: Tupla que contiene la información del usuario.
    """
    return conn_usuario.get_usuario(id)  

@app.delete('/usuarios/{id}')
def delete_usuario(id: str) -> dict:
    """
    Elimina el usuario con el id especificado.

    Args:
        id (str): id del usuario que se desea eliminar.

    Returns:
        dict: Mensaje de confirmación en caso de que el usuario exista.
    """
    conn_usuario.delete_usuario(id)
    return {"message": "El usuario ha sido eliminado satisfactoriamente"}

@app.put('/usuarios/{id}')
def update_usuario(updatedUsuario: Usuario,id:str) -> dict:
    """
    Actualiza la información del usuario con el id especificado.

    Args:
        updatedUsuario (Usuario): Datos que se desean actualizar en el usuario.
        id(str): id del usuario que se desea actuzalizar

    Returns:
        dict: Mensaje de confirmación.
    """
    data=updatedUsuario.dict()
    data['id']=id
    conn_usuario.update_usuario(data)
    return {"message": "El usuario se ha actualizado satisfactoriamente"}

@app.post('/docente')
def save_docente(docente: Docente) -> None:
    """
    Crea el registro del docente.

    Args:
        docente (Docente): Datos del docente.
    """
    data = docente.dict()
    conn_docente.write(data)

@app.get('/docente')
def get_docentes() -> list:
    """
    Muestra todos los docentes registrados.

    Returns:
        list: Lista que contiene los docentes.
    """
    return conn_docente.read_all()

@app.get('/docente/{id}')
def get_docente(id: str) -> tuple:
    """
    Muestra los datos del docente, si existe.

    Args:
        id (str): id del docente.

    Returns:
        tuple: Datos del docente.
    """
    return conn_docente.get_docente(id)

@app.delete('/docente/{id}')
def delete_docente(id: str) -> dict:
    """
    Elimina el docente con el id especificado

    Args:
        id (str): id del docente

    Returns:
        dict: Mensaje de confirmación.
    """
    conn_docente.delete_docente(id)
    return {"message": "El docente ha sido eliminado satisfactoriamente"}

@app.put('/docente/{id}')
def update_docente(updatedDocente: Docente,id:str) -> dict:
    """
    Actualiza la información del docente con el id especificado.

    Args:
        updatedDocente (Docente): Datos que se desean actualizar en el docente.
        id(str): id del docente que se desea actualizar

    Returns:
        dict: Mensaje de confirmación.
    """
    data=updatedDocente.dict()
    data['id']=id
    conn_docente.update_docente(data)
    return {"message": "El docente se ha actualizado satisfactoriamente"}


@app.post('/curso')
def save_curso(curso: Curso) -> None:
    """
    Crea el registro del curso.

    Args:
        curso (Curso): Datos del curso.
    """
    data = curso.dict()
    conn_curso.write(data)

@app.get('/cursos')
def get_cursos() -> list:
    """
    Muestra la lista de cursos disponibles.

    Returns:
        list: Lista que contiene los cursos disponibles.
    """
    return conn_curso.read_all()

@app.get('/cursos/{id}')
def get_curso(id: str) -> tuple:
    """
    Muestra la información del curso con el id especificado.

    Args:
        id (str): id del curso.

    Returns:
        tuple: información del curso.
    """
    return conn_curso.get_curso(id)
    
@app.delete('/cursos/{id}')
def delete_curso(id: str) -> dict:
    """
    Elimina el curso con el id especificado

    Args:
        id (str): id del curso.

    Returns:
        dict: Mensaje de confirmación.
    """
    conn_curso.delete_curso(id)        
    return {"message": "El curso ha sido eliminado satisfactoriamente"}

@app.put('/cursos/{id}')
def update_curso(updatedCurso: Curso,id:int) -> dict:
    """
    Actualiza la información del curso con el id especificado.

    Args:
        updatedCurso (Curso): Datos que se desean actualizar en el curso.
        id (str): id del curso que se desea actualizar

    Returns:
        dict: Mensaje de confirmación.
    """
    data=updatedCurso.dict()
    data['id']=id
    conn_curso.update_curso(data)
    return {"message": "El curso se ha actualizado satisfactoriamente"}

@app.post('/carritocompras')
def save_compra(carrito: Carrito_compra) -> None:
    """
    Crea el registro de compra.

    Args:
        carrito (Carrito_compra): Datos de la compra
    """
    data = carrito.dict()
    conn_carrito.write(data)

@app.get('/carritocompras/{id}')
def get_total(id: str) -> Conexioncarrito:
    """
    Calcula el total a pagar del usuario especificado con el id.

    Args:
        id (str): id del usuario.

    Returns:
        Conexioncarrito: Valor total a pagar.
    """
    total=conn_carrito.factura_total(id)
    return {"message":f'El total a pagar es {total[0]}'}

@app.get('/carritocompras/docente/{id}')
def get_total_docente(id: str) -> Conexioncarrito:
    """
    Calcula el total a pagar al docente por los cursos que imparte.

    Args:
        id (str): id del docente.

    Returns:
        Conexioncarrito: Valor total a pagar.
    """
    total=conn_carrito.pago_docente(id)
    if total==None:
        raise HTTPException(status_code=404, detail="El docente todavia no tiene pago disponible")
    else:
        return {"message":f'El total a pagar al docente {total[0]} es {total[1]}'}
