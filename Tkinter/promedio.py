import tkinter as tk
from tkinter import messagebox

#función para calcular promedio
def calcular_promedio():
    nombre = entrada_nombre.get().strip()
    try:
        cal1 = float(entrada_cal1.get().strip())
        cal2 = float(entrada_cal2.get().strip())
        cal3 = float(entrada_cal3.get().strip())

        #validar calificacionnes solo del 6 al 10
        for cal in [cal1,cal2,cal3]:
            if cal <6 or cal >10:
                #opc
                #6 <= cal <= 10
                messagebox.showerror("Error", "ingresa calificación del 6 al 10")
            else:
                promedio = (cal1+cal2+cal3)/3
                if promedio >= 7:
                    estatus = "Aprobado"
                else:
                    estatus = "Reprobado"
#si haces text.get ("1.0",tk.end)
                resultado.delete("1.0",tk.END)#fila 1 columna 0
                resultado.insert(tk.END, f"Nombre del alumno:  {nombre}\n")
                resultado.insert(tk.END, f"promedio Final:  {promedio:.2f}\n")
                resultado.insert(tk.END, f"status:  {estatus}\n")
    except ValueError:
        messagebox.showerror("Error","Ingresa calificaciones numericas validas (6 a 10)")
    


ventana = tk.Tk()
ventana.title("Evaluación Alumno")
ventana.geometry("350x150")

tk.Label(ventana, text="Nombre del Alumno").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady = 5)

#calificaciones
tk.Label(ventana, text="calificación 1: ").pack()
entrada_cal1 = tk.Entry(ventana)
entrada_cal1.pack(pady = 5)

tk.Label(ventana, text="calificación 2: ").pack()
entrada_cal2 = tk.Entry(ventana)
entrada_cal2.pack(pady = 5)

tk.Label(ventana, text="calificación 3: ").pack()
entrada_cal3 = tk.Entry(ventana)
entrada_cal3.pack(pady = 5)

#boton
tk.Button(ventana, text ="calcular Promedio", command=calcular_promedio).pack(pady = 5)

resultado = tk.Text(ventana, height = 5 , width = 40)
resultado.pack()#empaquetamos

#
ventana.mainloop()


