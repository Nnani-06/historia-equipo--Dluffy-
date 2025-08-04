import tkinter as tk

def saludar():
    nombre = entrada.get()
    edad = entrada.get()
    matricula = entrada.get()

    mensaje = f"Hola {nombre.capitalize()} tienes {edad} años de edad y con una matricula que es {matricula}"

ventana = tk.Tk()
ventana.title("Datos Alumno")
ventana.geometry("300x150")
ventana.configure(bg ="lightpink")

etiqueta1 = tk.Label(ventana, text = "Ingresa tu Nombre")
etiqueta2 = tk.Label(ventana, text = "Ingresa tu edad")
etiqueta3 = tk.Label(ventana, text = "Ingresa tu Matricula")

entrada = tk.Entry(ventana) #entrada
entrada.pack(pady = 20)




entrada = tk.Entry()
entrada.pack(pady = 20)

boton = tk.Button(ventana, text = "Iniciar", command = saludar)
boton.pack(pady = 3)

ventana.mainloop()