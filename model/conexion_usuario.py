import psycopg2

from utils.env_variables import Env_variables

env_variables= Env_variables()

DB_NAME= env_variables.db_name
DB_USER= env_variables.db_user
DB_PASS= env_variables.db_pass
DB_HOST= env_variables.db_host
DB_PORT= env_variables.db_port


class Conexionusuario():
    conn = None
    
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
        except psycopg2.OperationalError as err:    
            print(err)
            self.conn.close()
    

    def write(self, data) -> None:
        """
        Este método inserta los valores a la tabla usuario
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "usuarios"(id,nombre,fecha_creacion,email) VALUES(%(id)s,%(nombre)s,%(fecha_creacion)s,%(email)s) 
            """,data)
        self.conn.commit()

    def read_all(self) -> list:
        """
        Este método muestra los usuarios registrados.
        """
        with self.conn.cursor() as cur:      
            cur.execute("""
            SELECT * FROM "usuarios"
            """)
            data = cur.fetchall()
            return  data
    
    def get_usuario(self,id) -> tuple:
        """
        Este método busca el usuario por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM "usuarios" where id = %s
            """,(id,)) 
            data = cur.fetchone()
            return data 

    def delete_usuario(self,id) -> None:
        """
        Este método elimina el usuario por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "usuarios" where id =  %s
            """,(id,)) 
        self.conn.commit() 

    def update_usuario(self,data) -> None:
        with self.conn.cursor() as cur:
            cur.execute("""
            UPDATE "usuarios" SET nombre = %(nombre)s,email = %(email)s WHERE id = %(id)s
            """,data) 
        self.conn.commit()    

    def __def__(self) -> None:
        self.conn.close()