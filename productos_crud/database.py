import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "Dluffy06"     # Si tu MySQL tiene contraseña, ponla aquí
        self.__database = "inv_productos"

        self.conn = None#no hay connexion
        self.cursor  = None #no hay consultas
    
    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host =self.__host,
                user = self.__user,
                password = self.__password,
                database = self.__database
            )

            self.cursor =self.conn.cursor() #utilizanos un cursor con una conexion activa
            #self._create_tables()

        except mysql.connector.Error as e:
            print(f"Error en la conexión {e}")
            return None
        
    def _create_tables(self):
        #creamos las tablas si no existen
        self.cursor.execute(
            '''
                CREATE TABLE IF IS NOT EXIST categorias(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL 
        )
            '''
        )
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXIST productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                precio DECIMAL(10,2) NOT NULL,
                id_categoria INT,
                FOREIGN KEY (id_categoria) REFERENCES categorias(id)
                )
            '''
        )
        #confirmar creacion de tablas
        self.conn.commit()

    def close(self):
        #cerramos el cursor y la conexión 
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

conexion = DatabaseConnection()
conexion.conectar()

