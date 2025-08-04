class Estudiante:
    def __init__(self,nombre,edad,calificaciones):#cuando se manda el objeto se manda el shelf
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def calcular_pomedio(self): #como es clase si tiene self
        suma_calif = 0

        #for calif in self.calificaciones:
           # suma_calif += self.calificacion

        for i in range(len(self.calificaciones)):
            suma_calif += self.calificaciones[i]
        #for calificacion in ennumerate(self.calificaciones):
           # suma_calif += calificacion ¡no funciona! es una tupla

        promedio = suma_calif/ len(self.calificaciones)
        print (f"{self.nombre} tiene promedio de : {promedio:.2f}")

estudiante1 = Estudiante("daniela",19,[8.5,9.2,6,5])
estudiante2 = Estudiante("Moli" , 21 , [8.5,7.9,8.0])
estudiante3 = Estudiante("Fer", 18,[9,10,8])

estudiante1.calcular_pomedio()
estudiante2.calcular_pomedio()
estudiante3.calcular_pomedio()





#shelf ¿?