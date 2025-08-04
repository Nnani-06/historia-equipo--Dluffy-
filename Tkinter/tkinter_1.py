#pract modular
import tkinter as tk
#root , ventana
root = tk.Tk()
root.title("Mi primera Gui")
root.geometry("300x100")

mensaje = tk.Label(root,text ="¡Hola Mundo!")#laber mensajes con texto
#mensaje.pack()
mensaje.pack(padx = 90,pady = 50)#pady espaciado

root.mainloop()