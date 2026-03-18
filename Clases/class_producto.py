class Producto: # Clase principal de los proyectos
    def __init__ (self, id_producto, nombre, descripción, categoría, precio, unidad):
        self.id_producto = id_producto 
        self.nombre = nombre 
        self.descripción = descripción 
        self.categoría = categoría  # Instancia de la clase Categoria
        self.precio = precio # Precio del producto   
        self.unidad = unidad  # Unidad de medida (ej: 'pieza', 'kg', etc.)

    def __str__(self):
        return (f"Producto: {self.nombre} (ID: {self.id_producto})\n"
                f"Descripción: {self.descripción}\n"
                f"Categoría: {self.categoría.nombre}\n"
                f"Precio: ${self.precio}\n"
                f"Unidad: {self.unidad}\n")
        

