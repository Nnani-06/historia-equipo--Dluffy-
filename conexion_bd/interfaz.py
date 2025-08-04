# interfaz.py
import tkinter as tk
from producto import Producto

def mostrar_productos():
    texto.delete("1.0", tk.END)
    for idx, nombre, precio, categoria in producto_obj.mostrar_productos():
        linea = f"ID:{idx} | {nombre} | ${precio:.2f} | {categoria}\n"
        texto.insert(tk.END, linea)

if __name__ == "__main__":
    producto_obj = Producto()

    ventana = tk.Tk()
    ventana.title("Inventario de Productos")
    ventana.geometry("500x400")

    btn_mostrar = tk.Button(ventana, text="Mostrar productos", command=mostrar_productos)
    btn_mostrar.pack(pady=10)

    texto = tk.Text(ventana, width=60, height=20)
    texto.pack(padx=10, pady=10)

    ventana.mainloop()
