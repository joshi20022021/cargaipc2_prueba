from nodo import Nodo

# Definición de la clase Cancion que utiliza el nodo para la lista doblemente enlazada

class Cancion:
    def __init__(self, nombre, artista, album, imagen, ruta):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.ruta = ruta
        self.nodo = Nodo(self)