class Categoria:
    """
    Clase para representar una categoría en el inventario de películas y videojuegos.
    """
    
    def __init__(self, id_categoria, nombre, tipo, genero, descripcion=""):
        """
        Inicializa una categoría.
        
        Args:
            id_categoria: ID único de la categoría
            nombre: Nombre de la categoría
            tipo: Tipo de contenido ('película' o 'videojuego')
            genero: Género (ej: acción, aventura, drama, etc.)
            descripcion: Descripción opcional de la categoría
        """
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.tipo = tipo
        self.genero = genero
        self.descripcion = descripcion
        self.cantidad = 0  # Cantidad de items en esta categoría
    
    def __str__(self):
        """Representación en texto de la categoría."""
        return f"Categoría: {self.nombre} | Tipo: {self.tipo} | Género: {self.genero}"
    
    def __repr__(self):
        """Representación oficial de la categoría."""
        return f"Categoria(id={self.id_categoria}, nombre='{self.nombre}', tipo='{self.tipo}', genero='{self.genero}')"
    
    def actualizar_cantidad(self, cantidad):
        """Actualiza la cantidad de items en la categoría."""
        self.cantidad = cantidad
    
    def incrementar_cantidad(self, cantidad=1):
        """Incrementa la cantidad de items."""
        self.cantidad += cantidad
    
    def decrementar_cantidad(self, cantidad=1):
        """Decrementa la cantidad de items."""
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
        else:
            print(f"Error: No hay suficientes items. Cantidad disponible: {self.cantidad}")
    
    def obtener_informacion(self):
        """Retorna la información completa de la categoría."""
        return {
            'id': self.id_categoria,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'genero': self.genero,
            'descripcion': self.descripcion,
            'cantidad': self.cantidad
        }
