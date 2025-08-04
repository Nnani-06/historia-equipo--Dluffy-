##vamos a ocupar clase pidiendo las calificaciónes el nombre y edad

class estudiante:
    def __init__(self,nombre,edad):#cuando se manda el objeto se manda el shelf
        self.nombre=nombre
        self.edad=edad
        self.suma_calificaciones =0.0

    def agregar_calif(self, calificacion):
        self.calificacion +=calificacion

        #no son atributos se ocuparán para el promedio , no se guardara
        #self.suma_calif=0.0
        #self.cant_calif=0

    def calcular_promedio(self):
        promedio=self.suma_calificaciones / cantidad
        print(f"{self.nombre} tiene como promedio {promedio:.2f}")

nombre=input("Dame tu nombre:  ")
edad=int(input("dame tu edad:  "))

estudiante=estudiante(nombre,edad)
cantidad=0

while cantidad <= 2:
    try:
        calificacion =float(input(f"ingresa la calificación {cantidad+1}"))
        if calificacion<6 or calificacion>10:
            print("Error , la calificación debe estar entre el 6 y entre el 10")
        else:
            estudiante.agregar_calif(calificacion)
            cantidad += 1
    except ValueError:
        print("Error: ingresa un numero valido")

estudiante.calcular_promedio(cantidad)


            