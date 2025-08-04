# producto.py
from conexion import Conexion

class Producto:
    def __init__(self):
        # Instanciamos la conexión
        self.conexion = Conexion().conectar()
        if not self.conexion:
            raise Exception("No se pudo establecer conexión con la base de datos")

    def mostrar_productos(self):
        """
        Devuelve lista de tuplas:
        (id_producto, nombre_producto, precio, nombre_categoria)
        """
        cursor = self.conexion.cursor()
        query = """
            SELECT p.id, p.nombre, p.precio, c.nombre
            FROM productos p
            JOIN categorias c ON p.id_categoria = c.id;
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

if __name__ == "__main__":
    # Prueba rápida (eliminar más adelante)
    p = Producto()
    for fila in p.mostrar_productos():
        print(fila)

