def listar_productos(productos):
    for producto in productos:
        print ("----------------------------")
        print(producto)
        print ("----------------------------")

def agregar_categorias ():
    id_categoria = int(input("Ingresa el ID de la categoría que deseas agregar: "))
    nombre = input ("Ingresa el nombre de la categoría: ")
    tipo = input ("Ingresa el tipo de categoría (película o videojuego): ")
    genero = input ("Ingresa el género de la categoría: ")
    descripcion = input ("Ingresa una descripción para la categoría: ")
    from Clases.class_categoria import Categoria
    nuevo_producto = Categoria (id_categoria, nombre, tipo, genero, descripcion)
    return nuevo_producto 
