
class usuarios:
    def __init__(self,nombre,edad):
        self.__edad = edad
        self.nombre = nombre
    def mostrar_info(self):
        print(f"nombre ,{self.nombre} tiene de edad {self.__edad}")
       
    
    def get_edad(self):
        return self.__edad
    def set_edad(self,nva_edad):
        if nva_edad >= 0:
           self.__edad = nva_edad
        else:
             print(f"no tiene ni edad el cliente {self.nombre}")
    

class cliente(usuarios):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        pass

class administrador(usuarios):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        pass

cliente_normal = cliente ("Andrea", 20)
cliente_normal.mostrar_info()

cuenta_administrador = administrador ("Joaquin" ,34)
cuenta_administrador.mostrar_info()

#print(cliente_normal.get_edad())
#cliente_normal.__edad = 0
#print(cliente_normal.get_edad())

print("cambiando la edad de cliente a -2")
cliente_normal.set_edad(-2)
print(cliente_normal.get_edad)
cliente_normal.mostrar_info()


