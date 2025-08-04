##vamos a ocupar clase pidiendo las calificaciónes el nombre y edad

class estudiante:
    def __init__(self,nombre,edad):#cuando se manda el objeto se manda el shelf
        self.nombre = nombre
        self.edad = edad
      
    def calcular_promedio(self,suma_calificacion,cantidad_calificaciones):
        promedio = suma_calificacion / cantidad
        print(f"{self.nombre} tiene como promedio {promedio:.2f}")

nombre=input("Dame tu nombre:  ")
edad=int(input("dame tu edad:  "))

estudiante=estudiante(nombre,edad)
cantidad = 1
suma = 0

while cantidad <= 3:
    try:
        calificacion =float(input(f"ingresa la calificación {cantidad}:  "))
        if calificacion <6 or calificacion>10:
            print("Error , la calificación debe estar entre el 6 y entre el 10")
        else:
            calificacion +=calificacion
            cantidad += 1
    except ValueError:
        print("Error: ingresa un numero valido")


estudiante.calcular_promedio(calificacion,3)


            