import psycopg2


class Conexioncarrito():
    conn = None
    
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(database = 'dream_team_education', user = 'postgres', password = 'juanpzp.17', host = 'localhost', port = 5432)
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
            SELECT sum(t2.costo) FROM "carrito_compras" t1 
            LEFT JOIN "cursos" t2 on t1.id_curso = t2.id
            LEFT JOIN "usuarios" t3 on t1.id_usuario = t3.id
            WHERE t3.id = %s
            """,(id))