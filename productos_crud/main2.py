# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import csv


from database import DatabaseConnection
from crud_productos import ProductoCRUD
from data_models import Producto


# --- Configuración de BD ---
db = DatabaseConnection()
db.conectar()
crud = ProductoCRUD(db)


# Variable para almacenar el ID del producto seleccionado.
# Se declara al inicio como global para conservar el ID del único producto seleccionado y así reutilizarlo en todas las funciones.
id_producto_seleccionado = None


# --- Carga de categorías para el Combobox ---
# En teoría esto debe estar en un nuevo archivo de crud_categorias
def cargar_categorias():
   """
   Esto debería estar en crud_categorias.py sin embargo lo creamos aquí para facilitar las cosas pero si tenlo presente para tener todo bien estructurado
   """
   db.cursor.execute('SELECT id, nombre FROM categorias')
   rows_categorias = db.cursor.fetchall()
   # Agregamos la categoría de prueba
   ids_categorias   = [None]
   nombre_categorias = ["Selecciona una categoría"]


   for row_categoria in rows_categorias:
       # Aunque serán listas separadas sus ID estaran "unidos" pues serán identicos
       # ids_categorias = [0, 1, 2, 3]
       # nombre_categorias = [Default, Fruta, Verduras, Lacteos]
       # Pero cuando usemos index es como si hicieramos
       # nombre_categorias = [0, 1, 2, 3]


       ids_categorias.append(row_categoria[0])
       nombre_categorias.append(row_categoria[1])
      
   return ids_categorias, nombre_categorias


categorias_ids, categorias_nombres = cargar_categorias()


# --- Funciones ---
def agregar():
   """
   Recoge los datos del formulario, valida y crea un nuevo producto en la base de datos,
   luego limpia los campos y actualiza la tabla de productos.


   - Muestra cuadros de diálogo de éxito o error.
   - Llama a limpiar_entradas() y mostrar_productos() para refrescar la interfaz.
   """
   try:
       nombre = entry_nombre.get().strip()
       precio  = float(entry_precio.get())
       id_categoria = combo_categoria.current()
       cat_id  = categorias_ids[id_categoria]


       if not nombre or cat_id is None:
           # Aquí ya no es necesario validar precio por la excepción
           raise ValueError("Todos los campos son obligatorios.")


       # Recordemos los keywords arguments
       producto = Producto(
           nombre = nombre,
           precio = precio,
           id_categoria = cat_id
       )


       crud.agregar_producto(producto)
       messagebox.showinfo("Éxito", "Producto agregado correctamente")
      
       # Limpiar los campos del formulario y refrescar la tabla
       limpiar_entradas()
       mostrar_productos()


   except ValueError as ve:
       # Captura errores de validación (campo vacío o precio inválido)
       messagebox.showerror("Validación", str(ve))
   except Exception as e:
       messagebox.showerror("Error al agregar producto", str(e))




def mostrar_productos():
   for row in tabla.get_children():
       tabla.delete(row)


   try:
       productos = crud.obtener_productos()
       for producto in productos:
           tabla.insert('', tk.END, values = (
               producto.id,
               producto.nombre,
               f"{producto.precio:.2f}",
               producto.categoria_nombre
           ))
   except Exception as e:
       messagebox.showerror("Error al leer productos", str(e))




def seleccionar(event):
   """
   Captura la fila seleccionada en la tabla y pobla los campos del formulario con los datos del producto, además de guardar el ID para futuras acciones.


   Tenemos un evento disparado al seleccionar una fila en el Treeview.


   Además:
   - Rellenamos los Entry de ID, nombre y precio.
   - Ajusta el Combobox a la categoría correspondiente.
   - Deshabilita el botón 'Agregar' para evitar inserciones mientras se edita.
   """
   global id_producto_seleccionado


   # Obtener el identificador interno de la fila seleccionada en la tabla
   producto_seleccionado = tabla.selection()
  
   if not producto_seleccionado:
       # Si no hay ninguna selección, salir sin hacer nada
       return


   # Esta es la estructura de una tabla
   '''
   producto_seleccionado = {
       'text': '',
       'image': '',
       'values': (3, 'Jugo de Naranja', 15.0, 'Bebidas'),
       'open': False,
       'tags': ()
   }
   '''


   # Vamos a extraer el tuple de valores: (id, nombre, precio, nombre_categoria) de los valores del item de la fila seleccionada
   valores = tabla.item(producto_seleccionado)["values"]


   # Ahora asignamos cada columna a su variable correspondiente
  
   id_prod = valores[0]
   nombre = valores[1]
   precio = valores[2]
   nom_categoria = valores[3]


   # Estos también los puedes obtener así:
   # id_prod, nombre, precio, nom_categoria = valores


   # Guardar el ID para usarlo en editar/eliminar en la variable global, para poder usarlo en las funciones de modificar y eliminar el id seleccionado
   id_producto_seleccionado = id_prod


   # Rellenamos los campos de tkinter
   entry_id.config(state = "normal")
   entry_id.delete(0, tk.END)
   entry_id.insert(0, id_prod)
   entry_id.config(state = "disabled")


   entry_nombre.delete(0, tk.END)
   entry_nombre.insert(0, nombre)


   entry_precio.delete(0, tk.END)
   entry_precio.insert(0, precio)


   # Ahora recordemos cómo se hizo el Combobox
   # Aunque ids_categorias y nombre_categorias parecían estar separados, sus indices en sus arreglo estaran "unidos" pues serán identicos


   # ids_categorias = [0, 1, 2, 3]
   # nombre_categorias = [Default, Fruta, Verduras, Lacteos]


   # Cuando usamos index() obtenemos el indice del arreglo. Es como si obtuvieramos
   # nombre_categorias = [0, 1, 2, 3]
   # Ya te diste cuenta que los indices de los nombre son iguales a los ID de la BD


   try:
       id_categoria = categorias_nombres.index(nom_categoria)
   except ValueError:
       id_categoria = 0 # Categoría por defecto si el nombre no se encuentra
   combo_categoria.current(id_categoria)


   btn_agregar.config(state='disabled')




def editar():
   """
   Actualiza el producto seleccionado con los valores ingresados en el formulario.


   Comprueba que haya un producto seleccionado, valida los campos de entrada, construye una instancia de Producto con el ID existente y los nuevos datos, envía la actualización a la base de datos y refresca la interfaz.
   """


   global id_producto_seleccionado
  
   if id_producto_seleccionado is None:
       messagebox.showwarning("Aviso", "Primero selecciona un producto.")
       return


   try:
       nombre = entry_nombre.get().strip()
       precio = float(entry_precio.get())
       index_categoria = combo_categoria.current()


       # Traducimos el índice del Combobox a un ID de las categoría ya guardadas
       cat_id  = categorias_ids[index_categoria]


       # Validar que todos los campos obligatorios estén completos
       if not nombre or cat_id is None:
           raise ValueError("Todos los campos son obligatorios.")


       prod = Producto(
           id = id_producto_seleccionado,
           nombre = nombre,
           precio = precio,
           id_categoria = cat_id
       )


       crud.actualizar_producto(prod)


       messagebox.showinfo("Éxito", "Producto actualizado correctamente")


       # Informar al usuario del éxito y refrescar la vista
       limpiar_entradas()
       mostrar_productos()


   except ValueError as ve:
       # Captura errores de validación (campo vacío o precio inválido)
       messagebox.showerror("Validación", str(ve))
   except Exception as e:
       # Captura cualquier otro error inesperado durante la actualización
       messagebox.showerror("Error al actualizar", str(e))




def eliminar():
   """
   Elimina el producto seleccionado de la base de datos tras confirmación del usuario.


   Comprueba que haya un producto seleccionado, pide confirmación vía diálogo, ejecuta la eliminación, y luego actualiza la interfaz limpiando los campos y recargando la lista de productos.
   """
   global id_producto_seleccionado


   if id_producto_seleccionado is None:
       messagebox.showwarning("Aviso", "Primero selecciona un producto.")
       return


   # Pedir confirmación antes de eliminar
   if not messagebox.askyesno("Confirmar", "¿Eliminar producto seleccionado?"):
       return


   try:
       # Ejecutar la operación de borrado en la base de datos
       crud.eliminar_producto(id_producto_seleccionado)
       # Informar al usuario del éxito
       messagebox.showinfo("Éxito", "Producto eliminado correctamente")
       # Limpiar formulario y refrescar tabla
       limpiar_entradas()
       mostrar_productos()
      
   except Exception as e:
       # Capturar e informar problemas durante la eliminación
       messagebox.showerror("Error al eliminar", str(e))


def exportar_csv():
   # Pedimos al usuario la ruta de guardado
   ruta_csv = filedialog.asksaveasfilename(
       defaultextension=".csv",
       filetypes=[("Archivos CSV","*.csv")],
       title="Guardar productos como…"
   )


   if not ruta_csv:
       return  # El usuario canceló


   try:
       productos = crud.obtener_productos()
       # Creamos el archivo CSV
       with open(ruta_csv, mode="w", newline="") as archivo:
           # Definimos una variable que sería como el puntero en formato csv que escribirá en el archivo
           writer = csv.writer(archivo)
           # Escribirmos una fila con las cabeceras de la tabla
           writer.writerow(["ID", "Nombre", "Precio", "Categoría"])
           # Escribirmos una fila los datos de las instancias hechas a la clase Producto al hacer el SELECT
           for p in productos:
               writer.writerow([
                   p.id,
                   p.nombre,
                   f"{p.precio:.2f}",
                   p.categoria_nombre
               ])
       messagebox.showinfo("Exportado", f"Datos exportados a {ruta_csv}")
   except Exception as e:
       messagebox.showerror("Error", f"No se pudo exportar: {e}")




def limpiar_entradas():
   global id_producto_seleccionado
   id_producto_seleccionado = None


   entry_id.config(state='normal')
   entry_id.delete(0, tk.END)
   entry_id.config(state='disabled')


   entry_nombre.delete(0, tk.END)
   entry_precio.delete(0, tk.END)
   combo_categoria.current(0)
   combo_categoria.selection_clear()
   btn_agregar.config(state='normal')




# --- GUI ---
app = tk.Tk()
app.title("Gestión de Productos MySQL")
app.geometry("700x500")
padx, pady = 10, 5


# ID (solo lectura)
tk.Label(app, text="ID").pack(anchor='w', padx=padx, pady=(pady,0))
entry_id = tk.Entry(app, state='disabled')
entry_id.pack(fill='x', padx=padx)


# Nombre
tk.Label(app, text="Nombre").pack(anchor='w', padx=padx, pady=(pady,0))
entry_nombre = tk.Entry(app)
entry_nombre.pack(fill='x', padx=padx)


# Precio
tk.Label(app, text="Precio").pack(anchor='w', padx=padx, pady=(pady,0))
entry_precio = tk.Entry(app)
entry_precio.pack(fill='x', padx=padx)


# Categoría
tk.Label(app, text="Categoría").pack(anchor='w', padx=padx, pady=(pady,0))
combo_categoria = ttk.Combobox(app, values=categorias_nombres, state='readonly')
combo_categoria.current(0)
combo_categoria.pack(fill='x', padx=padx)


# Botones
frame_btn = tk.Frame(app)
frame_btn.pack(pady=pady)
btn_agregar = tk.Button(frame_btn, text="Agregar",   command=agregar)
btn_editar  = tk.Button(frame_btn, text="Editar",    command=editar)
btn_eliminar= tk.Button(frame_btn, text="Eliminar",  command=eliminar)
btn_export  = tk.Button(frame_btn, text="Exportar CSV", command=exportar_csv)


for b in (btn_agregar, btn_editar, btn_eliminar, btn_export):
   b.pack(side='left', padx=5)


# Tabla de productos
columns = ('ID','Nombre','Precio','Categoría')
tabla = ttk.Treeview(app, columns=columns, show='headings', selectmode='browse')
for col in columns:
   tabla.heading(col, text=col)
tabla.pack(fill='both', expand=True, padx=padx, pady=pady)
tabla.bind('<<TreeviewSelect>>', seleccionar)


# Carga inicial
mostrar_productos()


app.mainloop()
db.close()



