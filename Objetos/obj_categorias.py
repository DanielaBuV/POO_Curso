"""Module creating predefined Categoria instances.

Preferred usage:
    python -m Objetos.obj_categorias
from the project root. That way the package
import machinery handles the relative import.

If the module is run directly (e.g. python Objetos\obj_categorias.py),
a fallback adjusts sys.path so the sibling `Clases` package can be
found and the script still works.
"""

try:
    # normal package import
    from ..Clases.class_categoria import Categoria
except ImportError:
    # fallback when executed as a standalone script
    import os, sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from Clases.class_categoria import Categoria
    from Functions.main import *


# Categorias para películas
Drama = Categoria(1, "Drama", "película", "drama", "Películas dramáticas que exploran emociones profundas.")
Accion = Categoria(2, "Acción", "película", "acción", "Películas llenas de acción y aventuras emocionantes.")
Aventura = Categoria(3, "Aventura", "película", "aventura", "Películas que llevan al expectador a explorar mundos nuevos y emocionantes.")
Comedia = Categoria(4, "Comedia", "película", "comedia", "Películas diseñadas para hacer reír y entretener.")
RPG = Categoria(5, "RPG", "película", "rol", "Películas de rol donde los expectadores asumen personajes y completan misiones.")
Terror = Categoria(6, "Terror", "película", "terror", "Películas que buscan asustar y crear suspenso.")
Deportes = Categoria(7, "Deportes", "película", "deportes", "Películas basadas en deportes populares.")
CienciaFiccion = Categoria(8, "Ciencia Ficción", "película", "ciencia ficción", "Películas que exploran conceptos futuristas y tecnológicos.")
Estrategia = Categoria(9, "Estrategia", "película", "estrategia", "Películas con trama de planificación y tácticas para superar desafíos.")
Musical = Categoria(10, "Musical", "película", "musical", "Películas que integran música y canciones en la narrativa.")

# Categorias para videojuevos 
Acción_aventura = Categoria(11, "Acción_aventura", "videojuego", "acción aventura","Combinación de combates y exploración (ej. The Legend of Zelda)")
Shooters = Categoria (12, "Shooters", "videojuego","Shooters disparos","En primera persona (FPS) o tercera persona (TPS)")
Rol_RPG = Categoria (13, "Rol_RPG", "videojuego", "rol RPG", "Enfoque en la narrativa y evolución del personaje.")
Estrategia = Categoria (14, "Estrategia", "videojuego", "estrategia", "Tiempo real (RTS) o por turnos")
Simulacion = Categoria (15, "Simulacion", "videojuego", "simulacion", "Deportes, conducción, vida (ej. Los Sims).")
Sandbox = Categoria (16, "Sandbox", "videojuego", "Sandbox", "Libertad total de movimiento e interacción")
Plataformas = Categoria (17, "Plataformas", "videojuego", "Plataforma", " Salto y esquiva en entornos 2D o 3D.")
Battle_Royale = Categoria (18, "Battle Royale", "videojuego", "Battle royale", "Supervivencia multijugador masivo")
Puzzles = Categoria (19, "Puzzles", "videojuego", "Puzzle / rompecabezas", "Consisten en alinear o juntar piezas de un mismo tipo para hacerlas desaparecer o ganar puntos.")
Party_games = Categoria (20, "Party games", "videojuego", "Party games","juegos diseñados para muchos jugadores (local o en línea), con controles sencillos, partidas rápidas y, usualmente, un alto nivel de caos y risas")

Categoria_peliculas = [Drama, Accion, Aventura, Comedia, RPG, Terror, Deportes, CienciaFiccion, Estrategia, Musical]
Categoria_videojuegos = [Acción_aventura, Shooters, Rol_RPG, Estrategia, Simulacion, Sandbox, Plataformas, Battle_Royale, Puzzles, Party_games]
"""
listar_productos(Categoria_peliculas)


Novela = Categoria (21, "Novela", "película", "novela", "Películas de narrativa extensa que exploran personajes y tramas complejas.")

Categoria_peliculas.append(Novela)
listar_productos(Categoria_peliculas)

Suspenso = Categoria (22, "Suspenso", "película", "suspenso", "Películas que mantienen al espectador en tensión y expectación.")

Categoria_peliculas.append(Suspenso)
listar_productos(Categoria_peliculas)

Fantasia = Categoria (23, "Fantasia", "película", "fantasía", "Películas que presentan mundos imaginarios y elementos mágicos.")
categoria_peliculas.append(Fantasia)
listar_productos(Categoria_peliculas)

for categoria in Categoria_videojuegos:
    print (categoria)
Deportes = Categoria (21, "Deportes", "videojuego", "deportes", "Videojuegos basados en deportes populares como fútbol, baloncesto, etc.")
Categoria_videojuegos.append(Deportes)
for categoria in Categoria_videojuegos:
    print (categoria)
"""

listar_productos(Categoria_peliculas)
nuevo_producto = agregar_categorias() 
Categoria_peliculas.append(nuevo_producto)
listar_productos(Categoria_peliculas)   

