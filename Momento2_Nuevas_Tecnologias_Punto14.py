class Producto:
    def _init_(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def registrar_producto(self, margen_de_venta, callback):
        self.precio_de_venta = self.costo / (1 - margen_de_venta)
        callback(self)

    def _str_(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nCosto: {self.costo}\nCantidad: {self.cantidad}\nPrecio de venta: {self.precio_de_venta}"

class Inventario:
    def _init_(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def imprimir_inventario(self):
        for producto in self.productos.values():
           print(producto)