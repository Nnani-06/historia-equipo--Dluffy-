from data_models import Producto
from mysql.connector import Error

class ProductoCRUD:
    def __init__(self, db_connection):
        self.conn =db_connection.conn
        self.cursor = db_connection.cursor #si son publicos pasan rapido, directo vaya

    def agregar_producto(self , producto):
        try:
            sql = '''
                INSERT INTO productos (nombre,precio, id_categoria)
                VALUES (%s,%s,%s)
            '''
            valores = (producto.nombre,producto.precio,producto.id_categoria)
            self.cursor.execute(sql, valores)
            self.conn.commit()

            #opcA: devolver el id recien insertado
            #return self.cursor.lastrowid

            #opcb : o bien devolver yn booleano segun rowcount
            return self.cursor.rowcount == 1

        except Error as e:
            self.conn.rollback()
            raise

    def obtener_productos(self):
        productos = []
        try:
            query = '''
                        SELECT productos.id, productos.nombre, productos.precio, categorias.id, categorias.nombre
                        FROM productos
                        INNER JOIN categorias ON productos.id_categoria = categorias.id
                        
            '''
            self.cursor.execute(query)
            #Por defecto cursor.fetchall() te devuelve una lista de tuplas
            rows = self.cursor.fetchall()

            for row in rows: #añade producto
                p= Producto (
                    id = row[0],
                    nombre =row[1],
                    precio = row[2],
                    id_categoria = row[3],
                    categoria_nombre = row[4]
                )
                productos.append(p)

        except Error as e:
            print(f"Error al leer los productos {e}")#manda mensaje de consola de el error
            raise #si lo vas a imprimir una capa arriba , es pbligatorio , puede ser label o un messagebox
        return productos
    
    def obtener_por_id(self, producto_id):
        try:
            sql = '''
                SELECT productos.id, productos.nombre, productos.precio, categorias.id, categorias.nombre
                FROM productos
                INNER JOIN categorias ON productos.id_categoria = categorias.id
                WHERE productos.id = %s
                '''
            self.cursor.execute(sql, (producto_id,))
            row = self.cursor.fetchone()

            if row:
                return Producto(
                    id = row[0],
                    nombre = row[1],
                    precio = row[2],
                    id_categoria = row[3],
                    categoria_nombre = row[4]
            )
        
            return None
        except Error as e:
           print(e)
           raise
    def actualizar_producto(self,producto):
        try:
            sql = "UPDATE productos SET nombre = %s, precio = %s, id_categoria = %s WHERE id = %s"
            
            valores=(producto.nombre,producto.precio,producto.id_categoria,producto.id)
            self.cursor.execute(sql,valores)
            self.conn.commit()
        except Error:
            #hay raise por que la gui mostrara el error obtenido a menos que haya un messagebox
            self.conn.rollback()
            raise

    def eliminar_producto(self, producto_id):
        try:
            sql = "DELETE FROM productos WHERE id = %s"
        # self.cursor.execute("DELETE FROM productos WHERE id =%s", (producto_id,))
            self.cursor.execute(sql, (producto_id,))
            self.conn.commit()

        except Error as e:
            self.conn.rollback()
            raise
