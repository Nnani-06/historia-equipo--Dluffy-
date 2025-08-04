class animal:
    def __init__(self,nombre,edad,sonido):
        self.nombre = nombre
        self.__edad = edad
        self.sonido = sonido
    #def get__edad(self):
        #return self.__edad:
    #def set__edad(self):

    #def hacer_sonido(self):
       # print ("pue como hacen los animales ")

    def mostrar_info(self):
        #hacer_sonido()
        print(f" {self.nombre} hace {self.sonido}")

class perro(animal):
    def __init__(self, nombre, edad,sonido):
        super().__init__(nombre, edad,sonido)
        self.ladra = ladra

    def ir_por_el_palo():
        
        print("le gusta ir por el palo cuando se lo lanzan")

        
class gato(animal):
    def __init__(self, nombre, edad,sonido):
        super().__init__(nombre, edad,sonido)
    def ronronea():
        print("al gato le gusta ronronear")

class pajaro(animal):
    def __init__(self, nombre, edad, sonido,accion):
        super().__init__(nombre, edad, sonido)
        self.accion = accion
    

m_perro = perro ("coqueta",8,"Guau","ladra")
m_perro.mostrar_info()
m_perro.ir_por_el_palo

m_gato = gato ("oli", 2 , "miau")
m_gato.mostrar_info()
m_gato.ronronea

m_pajaro = pajaro ("Lincon",4,"Pio")
m_pajaro.mostrar_info()
