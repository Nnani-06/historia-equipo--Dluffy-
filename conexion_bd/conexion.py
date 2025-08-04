# conexion.py
import mysql.connector

class Conexion:
    def __init__(self):
        # Parámetros de conexión:
        self.host = "localhost"
        self.user = "root"
        self.password = "Dluffy06"     # Si tu MySQL tiene contraseña, ponla aquí
        self.database = "inv_productos"

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conexion
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
            return None

if __name__ == "__main__":
    # Aquí solo pruebo, no dejo nada global
    conexion = Conexion().conectar()
    if conexion and conexion.is_connected():
        print("Conexión exitosa")
    conexion.close()
else:
        print("Error de conexión")
