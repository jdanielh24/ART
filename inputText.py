"""
Archivo: inputText.py

	Este archivo contiene la clase InputBox, la cual es utilizada para agregar un campo de entrada de datos.

	Importaciones:
		> pygame: módulo que permite la creación de videojuegos en dos dimensiones.
        > tkinter: módulo que provee un conjunto de herramientas GUI.
"""
import pygame as pg
from tkinter import *
from tkinter import messagebox


pg.init()

# Definir colores y fuente para el InputText
COLOR_INACTIVO = pg.Color('lightskyblue3')
COLOR_ACTIVO = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:
    """
        Clase utilizada para crear un campo de entrada de texto.
    """

    def __init__(self, x, y, w, h, texto='', pv=0.8):
        """
            Inicializar valores del InputText.

            Parámetros
            ----------
            x: int
                posición x del InputText
            y: int
                posición y del InputText
            w: int
                ancho del InputText
            h: int
                altura del InputText
            texto: string
                texto que almacenará el  InputText.
            pv: float
                Parámetro de vigilancia que regresará.

            Otros atributos
            ----------
            activo: bool
                True si está activado el InputText, False de lo contrario.
        """
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVO
        self.texto = texto
        self.txt_surface = FONT.render(texto, True, self.color)
        self.activo = False
        self.pv = pv

    def manejar_evento(self, evento):
        """
            Manejar los eventos del InputText.

            Parámetros
            ----------
            event: EventType
	            objeto que representa el evento			
        """
        if evento.type == pg.MOUSEBUTTONDOWN:
            # Si el usuario hizo click sobre el InputText
            if self.rect.collidepoint(evento.pos):
                # Indicar que está activo.
                self.activo = not self.activo
            else:
                self.activo = False
            # Cambiar el color actual del InputText.
            self.color = COLOR_ACTIVO if self.activo else COLOR_INACTIVO
        if evento.type == pg.KEYDOWN:
            if self.activo:
                if evento.key == pg.K_RETURN:
                    Tk().wm_withdraw()  # para ocultar la ventana principal que genera Tk
                    pv = float(self.texto)
                    # si el valor introducion en el InputText es menor que 0 o mayor que 1 no aceptarlo
                    if pv < 0 or pv > 1.0: 
                        messagebox.showinfo('Advertencia', 'El parámetro de vigilancia debe ser un valor dentre 0 y 1.0')
                    else:
                        self.pv = pv
                    self.texto = ''
                elif evento.key == pg.K_BACKSPACE: # borrar texto
                    self.texto = self.texto[:-1]
                else:
                    self.texto += evento.unicode
                # Renderizar texto.
                self.txt_surface = FONT.render(self.texto, True, self.color)

    def dibujar(self, ventana):
        """
            Dibujar el InputText en la ventana.

            Parámetros
        ----------
            ventana: pygame.Surface
	            objeto que representa la ventana para la aplicación.			
        """
        ventana.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(ventana, self.color, self.rect, 2)
    
    def getPV(self):
        """
            Obtener el valor de self.pv			
        """        
        return self.pv