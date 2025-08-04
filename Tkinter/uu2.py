import tkinter as tk
from tkinter import messagebox 

class Tarea: #clase padre
    
    def __init__(self, titulo): #define el titulo y se inicia como no completada la clase
        self.__titulo = titulo #título privado
        self.__completada = False #inicia como False

    def get_titulo(self): #getter para obtener el título
        return self.__titulo

    def set_titulo(self, nuevo_titulo): #setter para modificar el título
        self.__titulo = nuevo_titulo

    def esta_completada(self): #verifica si está completada
        return self.__completada

    def marcar_completada(self): #cambia el booleano a completada para proximamente ocuparlo
        self.__completada = True

    def marcar_pendiente(self): #función nueva para volver a poner la tarea como pendiente (False)
        self.__completada = False

    def tareacompleta(self): #ocupa el bolleano true para mandar el mensaje si no , no imprime nd ( por eso el if)
        return f"{self.__titulo} {'[Completado]' if self.__completada else '[Pendiente]'}"

    def __str__(self): #va a modificar el objeto a texto desde __str__ y lo regresa con ese "formato"
        return self.tareacompleta()

class TareaPrioritaria(Tarea): #clase hija que hereda de Tarea (HERENCIA)
    
    def __init__(self, titulo, prioridad): #añadimos prioridad además del título
        super().__init__(titulo) #hereda constructor de Tarea
        self.prioridad = prioridad #prioridad nueva

    def __str__(self): #POLIMORFISMO: redefinimos cómo se imprime esta clase hija
        return f"[Prioridad {self.prioridad}] {super().__str__()}"

class AdministradorTareas: #gestiona las tareas creadas
    
    def __init__(self): #inicializa la lista donde se guardan tareas 
        self.tareas = [] #guarda tareas 

    def agregartarea(self, titulo, prioridad=None): #agrega tarea nueva
        if prioridad: #si se escribe una prioridad
            tarea = TareaPrioritaria(titulo, prioridad) #usa clase hija si tiene prioridad
        else:
            tarea = Tarea(titulo) #usa clase normal
        self.tareas.append(tarea) #añade tarea a la lista
        messagebox.showinfo("Agregado", "Tarea agregada correctamente")

    def completar(self, almacenado): #marca como completada la tarea elegida por índice
        self.tareas[almacenado].marcar_completada()

    def marcar_pendiente(self, almacenado): #función nueva para marcar como pendiente
        self.tareas[almacenado].marcar_pendiente()

    def eliminar(self, almacenado): #elimina tarea seleccionada
        opc = messagebox.askyesno("¿Eliminar?", "¿Estás seguro de eliminar la tarea?")
        if opc:
            del self.tareas[almacenado]
            messagebox.showinfo("Eliminado", "Tarea eliminada correctamente")

    def modificar(self, almacenado, nuevo_titulo): #modifica el nombre con el nuevo
        self.tareas[almacenado].set_titulo(nuevo_titulo)

    def obtener_todas(self): #manda las tareas añadidas
        return self.tareas

def actualizar_lista(): #elimina la lista para luego ingresarla con los nuevos datos cambiados
    lista_tareas.delete(0, tk.END)
    for tarea in admin.obtener_todas():
        lista_tareas.insert(tk.END, str(tarea))

def editar_tarea(): #ve cuál tarea está seleccionada y la modifica con lo nuevo escrito
    seleccion = lista_tareas.curselection()
    nuevo_titulo = entrada.get()
    if seleccion and nuevo_titulo:
        admin.modificar(seleccion[0], nuevo_titulo)
        entrada.delete(0, tk.END) #limpia el campo
        actualizar_lista()

def marcar_pendiente(): #marca la tarea como pendiente
    seleccion = lista_tareas.curselection()
    if seleccion:
        admin.marcar_pendiente(seleccion[0])
        actualizar_lista()

# datos de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de tareas")
ventana.geometry("320x420")
ventana.configure(bg = "lightpink")

tk.Label(ventana, text = "Bienvenido al Gestor de tareas ").pack()
tk.Label(ventana, text = "Ingresa tus Tareas: ").pack()

# Instancia del administrador de tareas
admin = AdministradorTareas()

# Campo libre para el título de la tarea
entrada = tk.Entry(ventana, width=25)
entrada.pack(pady = 5)

# Campo opcional para prioridad
prioridad_entry = tk.Entry(ventana, width=25)
prioridad_entry.insert(0, "Prioridad (opc)/alta/baja") #texto predeterminado
prioridad_entry.pack(pady=3)

# Botón para agregar una nueva tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea")
boton_agregar.pack(pady=5)

# cuadro que muestra las tareas
lista_tareas = tk.Listbox(ventana, width=40)
lista_tareas.pack(pady=3)

# Botón para marcar una tarea como completada
boton_completar = tk.Button(ventana, text="Marcar como completada")
boton_completar.pack(pady=5)

# Botón para marcar como pendiente
boton_pen = tk.Button(ventana, text="Marcar como Pendiente")
boton_pen.pack(pady=5)

# Botón para eliminar una tarea
boton_eliminar = tk.Button(ventana, text="Eliminar tarea")
boton_eliminar.pack(pady=5)

# Botón para editar una tarea
boton_editar = tk.Button(ventana, text="Editar tarea")
boton_editar.pack(pady=5)

# Configuración de los comandos de los botones
boton_agregar.config(command=lambda: (
    admin.agregartarea(entrada.get(), prioridad_entry.get() if prioridad_entry.get() != "Prioridad (opcional)" else None),
    entrada.delete(0, tk.END), #limpia campo
    prioridad_entry.delete(0, tk.END), #limpia prioridad
    actualizar_lista()
) if entrada.get() else None)

boton_completar.config(command=lambda: (
    admin.completar(lista_tareas.curselection()[0]), #identifica qué tarea marcó
    actualizar_lista()
) if lista_tareas.curselection() else None)

boton_eliminar.config(command=lambda: (
    admin.eliminar(lista_tareas.curselection()[0]),
    actualizar_lista()
) if lista_tareas.curselection() else None)

boton_pen.config(command=marcar_pendiente) #llama a función para marcar pendiente
boton_editar.config(command=editar_tarea) #llama a función para editar

# Inicia el bucle principal 
ventana.mainloop()
