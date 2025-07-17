'''
Primer programa de ejemplo craedo con la libreria Manim
Creado por: Omar Chanel Ali Fuertes
'''

from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # Crea un círculo
        circle.set_fill(RED, opacity=0.5) # Rellena el círculo de color rojo
        self.play(Create(circle)) # Muestra la animación de creación del círculo