#main
#from copy import Error
import tkinter as tk
from tkinter import messagebox
from database import DatabaseConnection
from data_models import Producto
from crud_productos import ProductoCRUD

db =  DatabaseConnection() #creamos un objero que gestionara la bd

try:
    db.conectar()
except Exception as e:
    print(f"no fue podible realizar la conexión a la base de datos {e}")
    raise # a diferencia del cud este raise evita que el proyecto continue ya que recordekmos q un try
#except 

crud = ProductoCRUD(db)


#funciones
def agregar():
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        categoria_id = int(entry_categoria.get())

        producto = Producto(nombre = nombre, precio = precio, id_categoria= categoria_id)
        ingresado = crud.agregar_producto(producto)

        if ingresado:
            messagebox.showinfo("Exito","Producto agregado correctamente")
        else:
            messagebox.showwarning("aviso","no agregoo ningun producto")

        mostrar_prod()
        limpiar_entradas()

    except Exception as e:
        messagebox.showerror("Hubo un error en los datos",str(e))

def mostrar_prod():
    try:

        lista.delete(0, tk.END)
        productos = crud.obtener_productos()
        for producto in productos:
            text=f"{producto.id} - {producto.nombre} - ${producto.precio:.2f} - Categoria: {producto.categoria_nombre}"
            lista.insert(tk.END, text)
         

    except Exception as e:
        tk.Label(app, text =e).pack()

def seleccionar_prod(event):
    producto_seleccionado = lista.curselection()

    if not producto_seleccionado:
        return
    item = lista.get(producto_seleccionado[0])#obtienes el producto seleccionado 

    id_prod= int(item.split(" - ")[0])

    #buscamos prod en bd
    try:
        p = crud.obtener_por_id(id_prod)
        if not p:
            messagebox.showerror("Error","Hubo un error en la selección")
            return
        
        entry_id.config(state='normal')
        entry_id.delete(0, tk.END)
        entry_id.insert(0, p.id)
        entry_id.config(state='disabled')

        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, p.nombre)
        entry_precio.delete(0, tk.END)
        entry_precio.insert(0, p.precio)
        entry_categoria.delete(0, tk.END)
        entry_categoria.insert(0, p.id_categoria)

    except Exception as e:
        messagebox.showerror("Error al seleccionar", str(e))

def editar():
    try:
        prod= Producto(
            nombre = entry_nombre.get(),#con get obtiene la información de entry_nombre
            precio = float(entry_precio.get()),
            id_categoria = int(entry_categoria.get()),
            id= int(entry_id.get())
        )
        crud.actualizar_producto(prod)
        messagebox.showinfo("exito","Producto actualizado correctamente")
        mostrar_prod()
        limpiar_entradas()

    except Exception as e:
        messagebox.showerror("Hubo un error al actualizar",str(e))
       # return prod
    
def eliminar():#no se crea ninguna instancia
    try:
        prod_id=int(entry_id.get())

        if not messagebox.askyesno("Confirmar","Eliminar producto seleccionado"):
            return

        crud.eliminar_producto(prod_id)
        messagebox.showinfo("exito","Producto eliminado correctamente")
        mostrar_prod()
        limpiar_entradas()
    except Exception as e:
        messagebox.showerror("Hubo error al eliminar ", str(e))

def limpiar_entradas():
    entry_id.delete(0,tk.END)
    entry_nombre.delete(0,tk.END)
    entry_precio.delete(0,tk.END)
    entry_categoria.delete(0,tk.END)

app = tk.Tk()
app.title("Gestión de productos en MySQL")

entry_id = tk.Entry(app)
entry_id.pack()#encapsula
entry_id.config(state = "disabled")

#nombre producto
tk.Label(app, text = "Nombre").pack(pady = 5)
entry_nombre = tk.Entry(app)
entry_nombre.pack()

#precio
tk.Label(app, text = "Precio").pack(pady = 5)
entry_precio = tk.Entry(app)
entry_precio.pack()

#ctegoria
tk.Label(app, text = " Categoria").pack(pady =  5)
entry_categoria = tk.Entry(app)
entry_categoria.pack()

#botones de accion
frame_btns = tk.Frame(app)
frame_btns.pack(pady = 5)

btn_agregar = tk.Button(frame_btns,text="Agregar",command=agregar)
btn_agregar.pack(side = tk.LEFT, pady= 5)
btn_editar = tk.Button(frame_btns,text="editar",command=editar)
btn_editar.pack(side = tk.LEFT, pady= 5)
btn_eliminar = tk.Button(frame_btns,text="eliminar",command=eliminar)
btn_eliminar.pack(side = tk.LEFT, pady= 5)

#lista de productos
lista= tk.Listbox(app, width = 60)
lista.pack(fill = tk.BOTH, expand=True,padx=5,pady=5)#enpaquetado
lista.bind("<<ListboxSelect>>" , seleccionar_prod)
mostrar_prod()

app.mainloop()
db.close()