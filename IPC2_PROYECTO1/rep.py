import os
import tkinter as tk
from tkinter import filedialog
import pygame

class ReproductorMusica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Reproductor de Música")
        self.ventana.geometry("400x200")

        self.lista_canciones = []  # Lista de rutas de archivos mp3
        self.indice_cancion_actual = 0

        self.inicializar_gui()

    def inicializar_gui(self):
        # Etiqueta para mostrar el nombre de la canción actual
        self.etiqueta_cancion = tk.Label(self.ventana, text="", font=("Helvetica", 12))
        self.etiqueta_cancion.pack(pady=10)

        # Botones
        self.boton_cargar = tk.Button(self.ventana, text="Cargar Canciones", command=self.cargar_canciones)
        self.boton_cargar.pack(pady=20)

        self.boton_play = tk.Button(self.ventana, text="Play", command=self.play)
        self.boton_play.pack(side=tk.LEFT, padx=10)
        self.boton_pause = tk.Button(self.ventana, text="Pause", command=self.pause)
        self.boton_pause.pack(side=tk.LEFT, padx=10)
        self.boton_stop = tk.Button(self.ventana, text="Stop", command=self.stop)
        self.boton_stop.pack(side=tk.LEFT, padx=10)

    def cargar_canciones(self):
        # Abre el diálogo para seleccionar archivos de música
        archivos = filedialog.askopenfilenames(filetypes=[("Archivos de audio", "*.mp3")])

        # Agrega las canciones a la lista
        self.lista_canciones.extend(archivos)

        # Inicia la primera canción si no hay ninguna reproduciéndose
        if not pygame.mixer.music.get_busy() and self.lista_canciones:
            self.play()

    def play(self):
        if self.lista_canciones:
            pygame.mixer.init()
            pygame.mixer.music.load(self.lista_canciones[self.indice_cancion_actual])
            pygame.mixer.music.play()
            self.etiqueta_cancion.config(text=os.path.basename(self.lista_canciones[self.indice_cancion_actual]))

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    reproductor = ReproductorMusica(ventana_principal)
    ventana_principal.mainloop()