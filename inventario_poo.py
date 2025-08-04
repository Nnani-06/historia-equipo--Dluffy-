class fruta:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    def set_precio(self,nuevo_precio):
        if nuevo_precio >= 5 and nuevo_precio <=200:
            self.__precio = nuevo_precio

    def mostrar_info(self):
        print(f"Nombre {self.nombre.capitalize()} precio: {self.__precio}")

class inventario_frutas:
    def __init__(self):
        self.frutas ={}

    def mostrar(self):
        if not self.frutas:
            print("\nEl inventario esta vacio")
        else:
            print("\nInventario actual")
            for ide, objecto_fruta in self.frutas.items():   

                print(f"{ide} | ", end = "") #??
                objecto_fruta.mostrar_info()

    def agregar(self):
        id_fruta = input("ID de la fruta (ej.F001)").upper().strip()
        nombre = input ("Nombre de la fruta ").lower().strip()
        precio = float(input("Precio de la fruta").strip())

        self.frutas[id_fruta] = fruta(nombre, precio) 

    def eliminar(self):
        id_fruta= input("ID de fruta que quieres eliminar:  ").upper().strip()
        if id_fruta in self.frutas:
            del self.frutas[id_fruta]
            print(f"Fruta {id_fruta} ya eliminada")
        else:
            print(f"No se pudo eliminar la fruta con id {id_fruta}")

    def modificar(self):
        id_fruta= input("ID de fruta que quieres Modificar:  ").upper().strip()
        if id_fruta in self.frutas:
            
            nuevo= float(input("Nuevo precio de la fruta").strip())
            
            self.frutas[id_fruta].set_precio
            precio_actualizado = self.frutas [id_fruta].get_precio()

            print(f"El precio de la fruta {self.frutas} se cambi el precio a {precio_actualizado}" )
        else:
            print(f"la fruta con el id {id_fruta} no se encuentra")

#validar el ID,y precio , modificar nomrbre ,

def mostrar_menu():
    print("\n Menu de Inventario")
    print("1. Muestra Frutas")
    print("2. Agregar Frutas")
    print("3. Eliminar Frutas")
    print("4. Modifica el precio de la fruta")
    print("5. Salir")


def main():
    inventario = inventario_frutas()

    #carga de datos
    manzana = fruta("Manzana", 40.00)
    inventario.frutas["F001"] = manzana

    inventario.frutas.update({
        'F002': fruta("platano", 30.00),
        'F003': fruta("kiwi", 50.00)
    })

    while True:
        mostrar_menu()
        opcion = input("elije una opcion del 1-5:  ")
        if opcion == "1":
            inventario.mostrar()
        elif opcion == '2':
            inventario.agregar()
        elif opcion == '3':
            inventario.eliminar()
        elif opcion == '4':
            inventario.modificar()
        elif opcion == '5':
            print("\nHasta Luego")
            break
        else:
            print("Opcion no valida, por favor elige entre 1 hasta el 4")



if __name__ == "__main__":
    main()