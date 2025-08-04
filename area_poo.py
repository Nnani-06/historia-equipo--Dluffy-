
class figura:
    def __init__(self,nombre,lado,base,altura):
        self.nombre = nombre

        self.lado = lado
        self.base = base
        self.altura = altura

class cuadrado(figura):
    def __init__(self, nombre,lado):
        super().__init__(nombre,lado)
    def calcular_area_cuadrado(self,lado):
        a = (self.lado)*4

        print(f"la figura llamada {self.nombre} tiene un area de{a}")
    

class rectangulo(figura):
    def __init__(self, nombre,base,altura ):
        super().__init__(nombre,base,altura)

class triangulo(figura):
    def __init__(self, nombre, lado, base, altura):
        super().__init__(nombre, base, altura)

cuadradop = cuadrado("cuadrado",2)
triangulop = triangulo("triangulo")