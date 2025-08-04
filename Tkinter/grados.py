import tkinter as tk
from tkinter import messagebox


class Temperatura:
    def __init__(self,valor):
        self.valor = valor
        pass

class Celsius(Temperatura):
    def convertir(self):
        return (self.valor*9/5)+32

class Fahrenheit (Temperatura):
    def convertir(self):
        return (self.valor-32)*5/9


def convertir_temperatura():
    valor = float(entrada_temp.get().strip())
    tipo = opcion.get()
    if tipo == "Celsius":
        objeto_celsius = Celsius(valor)
        resultado = objeto_celsius.convertir()
        etiqueta_resultado.config(text = f"{valor}°C = {resultado:.2f}°F")
    else:
        objeto_Fahrenheit = Fahrenheit(valor)
        resultado = objeto_Fahrenheit.convertir()
        etiqueta_resultado.config(text = f"{valor}°F = {resultado:.2f}°C")



ventana = tk.Tk()
ventana.title("Conversión de temperatura")
ventana.geometry("300x200")
ventana.configure(bg = "lightblue")

tk.Label(ventana, text = "Temperatura:").pack()
entrada_temp = tk.Entry(ventana)
entrada_temp.pack(pady = 5)

opcion = tk.StringVar(value="Celsius")
tk.Radiobutton(ventana, text = "Celsius a Fahrenheit", variable = opcion,value = "Celsius").pack()

tk.Radiobutton(ventana, text = "Fahrenheit a Celsius", variable = opcion,value = "Fahrenheit").pack()

tk.Button(ventana, text = "Convertir" , command= convertir_temperatura).pack(pady = 10 )

etiqueta_resultado = tk.Label(ventana, text = "")
etiqueta_resultado.pack()

ventana.mainloop()
