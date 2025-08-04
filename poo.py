

class producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def mostrar(self): 
        print(f"producto: {self.nombre}, precio ${self.precio}")
        
p1 = producto("pan","25.0")
p2 = producto("agua","18.50")

p1.mostrar()
p2.mostrar()

