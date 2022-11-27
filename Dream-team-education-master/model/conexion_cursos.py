import psycopg2

class Conexioncursos():
    conn = None
    
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(database = 'dream_team_education', user = 'postgres', password = 'juanpzp.17', host = 'localhost', port = 5432)
        except psycopg2.OperationalError as err:    
            print(err)
            self.conn.close()
    

    def read_all(self) -> list:
        """
        Este método muestra los cursos disponibles.
        """
        with self.conn.cursor() as cur:      
            cur.execute("""
             SELECT * FROM "cursos"
            """)
            data = cur.fetchall()
            return data

    def write(self, data) -> None:
        """
        Este método inserta los valores a la tabla cursos
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "cursos"(id,curso,descripcion,costo,id_docente,docente,sesiones,duracion_sesion,calificacion,fecha_de_creacion) VALUES(%(id)s,%(curso)s,%(descripcion)s,%(costo)s,%(id_docente)s,%(docente)s,%(sesiones)s,%(duracion_sesion)s,%(calificaion)s,%(fecha_de_creacion)s) 
            """,data)
        self.conn.commit()

    def get_curso(self,id) -> tuple:
        """
        Este método busca el curso por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM "cursos" where id = %s
            """,(id,)) 
            data = cur.fetchone()
            return data 
    
    def delete_curso(self,id) -> None:
        """
        Este método elimina el curso por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "cursos" where id=%s
            """,(id,)) 
        self.conn.commit() 

    def update_curso(self,data) -> None:
        """
        Este método actualiza el curso por el id específico.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            UPDATE "cursos" SET curso = %(curso)s,descripcion = %(descripcion)s,costo = %(costo)s,id_docente = %(id_docente)s,docente = %(docente)s,sesiones = %(sesiones)s,duracion_sesion = %(duracion_sesion)s,calificacion = %(calificaion)s,fecha_de_creacion where = %(fecha_de_creacion)s WHERE id = %(id)s
            """,data) 
        self.conn.commit() 
    

    def __def__(self) -> None:
        self.conn.close()