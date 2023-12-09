import xml.etree.ElementTree as ET
from tkinter import filedialog
from tkinter import Tk
from cancion import Cancion
from nodo import Nodo

# Configurar la ventana de Tkinter para seleccionar el archivo
raiz = Tk()
raiz.withdraw()  # Ocultar la ventana principal

# Pedir al usuario que seleccione un archivo XML
archivo_xml = filedialog.askopenfilename(title="Selecciona un archivo XML", filetypes=[("Archivos XML", "*.xml")])

if archivo_xml:
    # Leer el archivo XML
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    # Crear una lista doblemente enlazada para almacenar las canciones
    lista_canciones = None
    canciones = root.findall('cancion')

    # Iterar sobre cada elemento 'cancion' en el XML y crear objetos Cancion
    for cancion in canciones:
        nombre = cancion.get('nombre')
        artista = cancion.findtext('artista')
        album = cancion.findtext('album')
        imagen = cancion.findtext('imagen')
        ruta = cancion.findtext('ruta')

        # Verificar si algún campo está vacío antes de crear el objeto Cancion
        if artista is not None and album is not None and imagen is not None and ruta is not None:
            nueva_cancion = Cancion(nombre, artista, album, imagen, ruta)
            
            # Agregar el objeto a la lista doblemente enlazada
            if lista_canciones is None:
                lista_canciones = nueva_cancion
            else:
                actual = lista_canciones
                while actual.nodo.siguiente:
                    actual = actual.nodo.siguiente.data
                actual.nodo.siguiente = Nodo(nueva_cancion)
                actual.nodo.siguiente.anterior = actual.nodo

     # Imprimir los datos de la lista doblemente enlazada hacia adelante
    actual = lista_canciones
    while actual:
        print(f"Nombre: {actual.nombre}, Artista: {actual.artista}, Album: {actual.album}, Imagen: {actual.imagen}, Ruta: {actual.ruta}")
        siguiente = actual.nodo.siguiente
        if siguiente:
            actual = siguiente.data
        else:
            break

    # Imprimir los datos de la lista doblemente enlazada hacia atrás
    ultimo = actual
    while ultimo:
        anterior = ultimo.nodo.anterior
        if anterior:
            ultimo = anterior.data
        else:
            break

    while ultimo:
        print(f"Nombre: {ultimo.nombre}, Artista: {ultimo.artista}, Album: {ultimo.album}, Imagen: {ultimo.imagen}, Ruta: {ultimo.ruta}")
        siguiente = ultimo.nodo.siguiente
        if siguiente:
            ultimo = siguiente.data
        else:
            break

else:
    print("No se seleccionó ningún archivo XML")