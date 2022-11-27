import psycopg2

class Conexiondocente():
    conn = None
    
    def __init__(self) -> None:
        try:
            self.conn=psycopg2.connect(database = 'dream_team_education', user = 'postgres', password = 'juanpzp.17', host = 'localhost', port = 5432)
        except psycopg2.OperationalError as err:    
            print(err)
            self.conn.close()
    

    def write(self, data) -> None:
        """
        Este método inserta los valores a la tabla docente
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "docente"(id,nombre,email,especialidad,fecha_creacion) VALUES(%(id)s,%(nombre)s,%(email)s,%(especialidad)s,%(fecha_creacion)s) 
            """,data)
        self.conn.commit()

    def read_all(self) -> list:
        """
        Este método muestra los docentes registrados.
        """
        with self.conn.cursor() as cur:      
            cur.execute("""
            SELECT * FROM "cursos"
            """)
            data = cur.fetchall()
            return data

    def get_docente(self,id) -> tuple:
        """
        Este método busca el docente por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM "docente" where id = %s
            """,(id,)) 
            data = cur.fetchone()
            return data 

    def delete_docente(self,id) -> None:
        """
        Este método elimina el docente por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "docente" where id = %s
            """,(id,)) 
        self.conn.commit() 

    def update_docente(self,data) -> None:
        """
        Este método actualiza el curso por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            UPDATE "docente" SET nombre = %(nombre)s,email = %(email)s,especialidad = %(especialidad)s WHERE id = %(id)s
            """,data) 
        self.conn.commit() 

    def __def__(self):
        self.conn.close()