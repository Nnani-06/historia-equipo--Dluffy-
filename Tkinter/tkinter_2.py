import tkinter as tk

def saludar():
    nombre = entrada.get() #obtiene lo que el usuario escribio
    mensaje = f"Hola {nombre.capitalize()}!"
    #etiqueta_resultado = tk.Label(ventana,text = mensaje)
    #etiqueta_resultado.pack()

    etiqueta_resultado.config(text = mensaje)#que le vas a configurar

ventana = tk.Tk()
ventana.title("Saludo personalizado")
ventana.geometry("300x150")

ventana.configure(bg = "lightblue")#bg background

#widget
#etiqueta = tk.label(ventana, text = "ingresa tu nombre",fg = "white",bg = "darkblue", font =("Arial",16))#fg forground
etiqueta = tk.Label(ventana, text = "ingresa tu nombre")
etiqueta.pack()

entrada = tk.Entry(ventana) #entrada
entrada.pack(pady = 20)

boton = tk.Button(ventana, text = "Saludar", command = saludar)
boton.pack(pady = 3)

etiqueta_resultado = tk.Label(ventana,text = "")
etiqueta_resultado.pack()


ventana.mainloop()# para que sea visto la ventana