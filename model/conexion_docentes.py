import psycopg2

class Conexiondocente():
    conn= None
    
    def __init__(self):
        try:
          self.conn=psycopg2.connect(database='dream_team_education', user='postgres', password='juanjose980107', host='localhost', port= 5432)
        except psycopg2.OperationalError as err:    
            print(err)
            self.conn.close()
    

    def write(self, data):
       with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "docente"(id,nombre,email,especialidad,fecha_creacion) VALUES(%(id)s,%(nombre)s,%(email)s,%(especialidad)s,%(fecha_creacion)s) 
            """,data)
       self.conn.commit()

    def read_all(self):
      with self.conn.cursor() as cur:      
         cur.execute("""
          SELECT * FROM "cursos"
         """)
         data=cur.fetchall()
         return  data

    def get_docente(self,id):
       with self.conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM "docente" where id=%s
        """,(id,)) 
        data=cur.fetchone()
        return data 

    def delete_docente(self,id):
       with self.conn.cursor() as cur:
        cur.execute("""
        DELETE FROM "docente" where id=%s
        """,(id,)) 
       self.conn.commit() 

    def update_docente(self,data):
        with self.conn.cursor() as cur:
         cur.execute("""
         UPDATE "docente" SET nombre=%(nombre)s,email=%(email)s,especialidad=%(especialidad)s WHERE id=%(id)s
         """,data) 
        self.conn.commit() 
       
               
    def __def__(self):
        self.conn.close()