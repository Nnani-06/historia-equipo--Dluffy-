import tkinter as tk
from tkinter import messagebox

class area:
    def __init__(self,nombre,base=0 , altura=0):
        self.nombre = nombre
        self.base = base
        self.altura = altura

class cuadrado(area):
    def __init__(self, nombre,lado):
        super().__init__(nombre)
        self.lado = lado
    def area_cuadrado(self):
        return self.lado*self.lado
    
class triangulo(area):
    def __init__(self, nombre,base,altura):
        super().__init__(nombre,base,altura)
    def area_triangulo(self):
        return (self.base*self.altura)/2
    
class rectangulo(area):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre, base, altura)
    def area_rectangulo(self):
        return (self.base * self.altura)
    
def convertir_area():
    valor=float(entrada_num.get().strip())
    tipo = opcion.get()
    if tipo == "cuadrado":
        tk.Label(ventana, text = "lado:").pack()
        lado_num = tk.Entry(ventana) 

        objeto_cuadrado = cuadrado(valor)
        resultado = objeto_cuadrado.convertir()
        etiqueta_resultado.config(text = f"{valor} = {resultado:.2f}")
    if tipo == "rectangulo":
        objeto_rectangulo = rectangulo(valor)
        resultado = objeto_rectangulo.convertir()
        etiqueta_resultado.config(text = f"{valor} = {resultado:.2f}")
    else:
        objeto_triangulo = triangulo(valor)
        resultado = objeto_triangulo.convertir()
        etiqueta_resultado.config(text = f"{valor} = {resultado:.2f}")
        


ventana = tk.Tk()
ventana.title("Area de Figuras")
ventana.configure(bg = "lightpink")
ventana.geometry("300x200")

tk.Label(ventana, text = "Bienvenido al Area :\n").pack()


tk.Label(ventana, text = "Dame el numero q quieres:").pack()
entrada_num = tk.Entry(ventana)
entrada_num.pack(pady = 5)

opcion = tk.StringVar(value="valor")
tk.Radiobutton(ventana, text = "Cuadrado", variable = opcion,value = "cuadrado").pack()
tk.Radiobutton(ventana, text = "Rectangulo", variable = opcion,value = "rectangulo").pack()
tk.Radiobutton(ventana, text = "Triangulo", variable = opcion,value = "triangulo").pack()

tk.Button(ventana, text = "Convertir" , command= convertir_area).pack(pady = 10 )

etiqueta_resultado = tk.Label(ventana, text = "")
etiqueta_resultado.pack()


    
    

ventana.mainloop()    