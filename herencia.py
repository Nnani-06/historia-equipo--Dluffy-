class persona: #clase padre
    def __init__(self,nombre , edad):
        self.nombre = nombre
        self.edad = edad

class alumno(persona): #Clase hija ,
    def  __init__(self, nombre, edad,calificaciones):
        super().__init__(nombre, edad) 
    #llama la información de la clase padre para posteriormente reutilizarlo en la clase hija
        self.calificaciones = calificaciones

    def calcular_primedio(self): #se pone self para poder llamar self. etc 
        suma = sum(self.calificaciones) #SUM es una suma jaja pero es mas facil 
                                        #escribirlo como math en java
        promedio = suma / len (self.calificaciones)
        print (f"{self.nombre} tiene calificación de {promedio:.2f}")

class maestro(persona):
    def __init__(self, nombre, edad,materia): #constructor,y en el init sin super se ingresa el nvo atributo
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_info(self):
        print(f"El maestr@ {self.nombre} de {self.edad} de edad , es maestro de {self.materia}")


alumno1 = alumno("Jair", 21 , [9,8,10])
alumno1.calcular_primedio()
maestro1 = maestro("David" , 26 , " POO ")
maestro1.mostrar_info()

#recuerda no solo por definir tienen que er¿star  afuera osea en la esquina ,
#  si es de la clase dejalo con la sangria correspondiente
