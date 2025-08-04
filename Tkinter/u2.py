import tkinter as tk
from tkinter import messagebox 

class Tarea: #clase padre
    
    def __init__(self, titulo): #define el titulo y se inicia como no completada la clase
    
        self.titulo = titulo
        self.completada = False

    def marcar_completada(self):#cambia el booleano a completada para proximamente ocuparlo
        self.completada = True

    def tareacompleta(self):#ocupa el bolleano true para mandar el mensaje si no , no imprime nd ( por eso el if)
        #return self.titulo + (" [Completada] " if self.completada else "")
        return f"{self.titulo} {'[Completado]' if self.completada else ''}"

    def __str__(self):#va a modificar el objeto a texto desde __str__ y lo regresa con ese "formato"
        return self.tareacompleta()
    
class tareaPrioritaria(Tarea):#def sin nada para modificarlo despues
        def prioritaria(self,prioridad):
          prioridad = prioridad.self
          return f"{self.titulo} {'' if self.completada else '[Pendiente]'}"
 

class AdministradorTareas:
    
    def __init__(self):
        
        self.tareas = []#guarda tareas 

    def agregartarea(self, titulo):
        tarea = Tarea(titulo) 
        self.tareas.append(tarea) #crea el objeto en la tarea aadiendola con el titulo y marcandola como no completada(por el false)
        messagebox.showinfo("hola","Agregado correctamente")
    
    def completar(self, almacenado): 
        self.tareas[almacenado].marcar_completada()
    
    def eliminar(self, almacenado):
        opc = messagebox.showerror("noo","Seguro que quieres eliminarlo? ")
        del self.tareas[almacenado]
        opc= messagebox.showinfo(":))","Eliminado correctaente")
            
    def modificar(self, almacenado, nuevo_titulo):#modifoca el nombre con el nuevo
        self.tareas[almacenado].titulo = nuevo_titulo

    def obtener_todas(self):#manda las tareas añadidas
        return self.tareas

def actualizar_lista():# elimina la lista para luego ingresarla con los nuevos datos cambiadosds
    lista_tareas.delete(0, tk.END)
    for tarea in admin.obtener_todas():
        lista_tareas.insert(tk.END, str(tarea))

def editar_tarea():
    seleccion = lista_tareas.curselection() #ve cuál tarea está seleccionada por el usuario en la lista
    nuevo_titulo = entrada.get() #identificas el nombre que eligio el usuario
    if seleccion and nuevo_titulo:
        admin.modificar(seleccion[0], nuevo_titulo) #ingresa el uevo titulo
        entrada.delete(0, tk.END)#eliminando el anterior para al actualizarse al nuevo
        actualizar_lista()

# datos de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de tareas")
ventana.geometry("300x350")
ventana.configure(bg = "lightpink")

tk.Label(ventana, text = "Bienvenido al Gestor de tareas ").pack()
tk.Label(ventana, text = "ingresa tus Tareas: ").pack()

# Instancia del administrador de tareas
admin = AdministradorTareas()

# Campo libre para el título de la tarea
entrada = tk.Entry(ventana, width=20)
entrada.pack(pady = 5)

# Botón para agregar una nueva tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea")
boton_agregar.pack(pady=5)

# cuadro que muestra las tareas
lista_tareas = tk.Listbox(ventana, width=30)
lista_tareas.pack(pady=3)

# Botón para marcar una tarea como completada
boton_completar = tk.Button(ventana, text="Marcar como completada")
boton_completar.pack(pady=5)

# Botón para editar una marcar como pendiente
boton_pen = tk.Button(ventana, text="Marcar como Pendiente")
boton_pen.pack(pady=5)

# Botón para eliminar una tarea
boton_eliminar = tk.Button(ventana, text="Eliminar tarea")
boton_eliminar.pack(pady=5)

# Botón para editar una tarea
boton_editar = tk.Button(ventana, text="Editar tarea")
boton_editar.pack(pady=5)

# Configuración de los comandos de los botones
boton_agregar.config(command=lambda: (#LAMBDA procesa eventos rapidos sin definir con def
    admin.agregartarea(entrada.get()),
    entrada.delete(0, tk.END),
    actualizar_lista()
) if entrada.get() else None)

boton_completar.config(command=lambda: (#mensiona si selecciono una tarea
    admin.completar(lista_tareas.curselection()[0]),#identifica que campo tomo para marcarla commo completada
    actualizar_lista()
) if lista_tareas.curselection() else None)#solo si toco una tarea si no no hace nd

boton_eliminar.config(command=lambda: (
    admin.eliminar(lista_tareas.curselection()[0]),
    actualizar_lista()
) if lista_tareas.curselection() else None)

boton_pen.config(tareaPendiente)
boton_editar.config(command=editar_tarea) 

# Inicia el bucle principal 
ventana.mainloop()
