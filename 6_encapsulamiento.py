
class perro:
    def __init__(self,nombre , edad , raza):
        self.nombre = nombre
        self.__edad = edad
        self.raza = raza
    
    def get_edad(self):
        return self.__edad
    def set_edad(self,nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else :
            print (" la edad no puede ser negativa")

    def mostrar_info(self):
        print(f"Nombre {self.nombre}")
        print(f"Edad {self.__edad} años")
        print(f"Raza: {self.raza}")


mi_perro = perro ("coqueta", 8 , "franche puddle")
print("informació de perro")
mi_perro.mostrar_info()

print(mi_perro.nombre)
print(mi_perro.get_edad())
mi_perro.__edad = 10
print(mi_perro.get_edad())
#print(mi_perro.__edad

print("\nCambiando la edad a 7...")
mi_perro.set_edad(7) # si quieres  sacar a diferentes clases ,define la inicialización
mi_perro.mostrar_info()

print("\nCambiando la edad a 3...")
mi_perro.set_edad(-3)
mi_perro.mostrar_info()