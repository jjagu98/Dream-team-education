import psycopg2
from utils.env_variables import Env_variables

env_variables= Env_variables()

DB_NAME= env_variables.db_name
DB_USER= env_variables.db_user
DB_PASS= env_variables.db_pass
DB_HOST= env_variables.db_host
DB_PORT= env_variables.db_port

class Conexioncarrito():
    conn = None
    
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
        except psycopg2.OperationalError as err:    
            print(err)
            self.conn.close()
    
    def write(self, data) -> None:
        """
        Este método inserta los valores a la tabla carrito_compras
        """
    
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "carrito_compras"(id_compra,id_usuario,id_curso) VALUES(%(id_compra)s,%(id_usuario)s,%(id_curso)s)
            """,data)
        self.conn.commit()
    
    def factura_total(self,id) -> None:
        """
        Este método calcula el total a pagar del usuario.
        """        
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT t3.nombre,sum(t2.costo) FROM "carrito_compras" t1 
            LEFT JOIN "cursos" t2 on t1.id_curso=cast(t2.id as int)
            LEFT JOIN "usuarios" t3 on t1.id_usuario=t3.id
            WHERE t3.id=%s
            GROUP BY t3.nombre
            """,(id,))
            data=cur.fetchone()
            return data
    
    def pago_docente(self,id) -> None:
        """
        Este método calcula el total a pagar al docente por los cursos que imparte.
        """        
        with self.conn.cursor() as cur:
            cur.execute("""
             select t2.docente, sum(t2.costo*0.6) as pago_comision_total from carrito_compras t1 
             left join cursos t2 on t1.id_curso=cast(t2.id as int) where t2.id_docente=%s 
             group by t2.docente
            """,(id,))
            data=cur.fetchone()
            return data
    
