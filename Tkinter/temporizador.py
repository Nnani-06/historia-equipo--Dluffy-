import tkinter as tk
from tkinter import messagebox # ventanas emergentes

def iniciar_temporizador():
    try:
        segundos = int(campo_tiempo.get())
        #minutos = int(campo_tiempo.get())

        if segundos > 5:
            cuenta_regresiva(segundos)
            etiqueta_resultado.config(text = f"¡Tiempo iniciado para {segundos} segundos!")
        else:
            messagebox.showerror("Advertencia","El tiempo a contar debe ser mayor o igual que 5 segundos")

    except ValueError:
        messagebox.showerror("Error" , "ingresa numero positivo")

def cuenta_regresiva(segundos):
    if segundos > 0:
        etiqueta_resultado.config(text = f"tiempo restante {segundos}s")
        ventana.after(1000, cuenta_regresiva, segundos - 1)# el segundo lo lee como 1000
    else:
        messagebox.showinfo("Temporizador"," Se acabo el tiempo ")
        messagebox.showinfo(":)","holaa")


ventana = tk.Tk()
ventana.title("Temporizador")
ventana.geometry("300x150")


etiqueta_instrucciones = tk.Label(ventana, text = "ingresa tiempo en segundos:  ")
etiqueta_instrucciones.pack(pady = 5)

campo_tiempo = tk.Entry(ventana)
campo_tiempo.pack(pady = 5)

#boton para temporizador
boton_iniciar = tk.Button(ventana, text = "iniciar", command = iniciar_temporizador)
boton_iniciar.pack(pady = 5)

#mostrar resultado
etiqueta_resultado = tk.Label(ventana, text = "")
etiqueta_resultado.pack(pady = 5)

ventana.mainloop()
