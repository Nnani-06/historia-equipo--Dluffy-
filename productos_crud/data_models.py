class categoria:
    def __init__(self, id = None , nombre = None):# primeros los que requieran datos , luego los que no , ya lo implemento python
        self.id = id
        self.nombre = nombre

class Producto:
    def __init__(self, id=None,nombre=None,precio=None,id_categoria=None,categoria_nombre=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.categoria_nombre = categoria_nombre