"""
Archivo: nodo.py

	Este archivo contiene la clase Nodo, utilizada para almacenar los atributos de cada casilla en la cuadrícula
	(si está activado o no, su posicion, etc).

	Importaciones:
		> pygame: módulo que permite la creación de videojuegos en dos dimensiones.
"""

import pygame


pygame.init()  # si se omite, no se crearán las fuentes. Se necesitan inicializar


class Nodo:
    """
        Clase utilizada para almacenar los atributos de cada casilla en la cuadricula.
    """

    def __init__(self, fila, columna, ancho, total_filas, x_inicial):
        """
            Inicializar valores del nodo.

            Parámetros
            ----------
            fila: int
                fila en que se encuentra el nodo.
            columna: int
                columna en que se encuentra el nodo.
            ancho: int
                ancho de la casilla del nodo.
            total_filas: int
                numero de filas que hay en la cuadricula donde se encuentra el nodo.
            x_inicial: int
                valor inicial de la coordenada x.

            Otros atributos
            ----------
            x: int
                posicion en el eje X donde se encuentra el nodo.
            y: int
                posicion en el eje Y donde se encuentra el nodo.
                        color: tuple
                                Tupla que representa el color del nodo.
                        activado: int
                                1 si está activado (seleccionado), 0 de lo contrario.
        """
        self.fila = fila
        self.columna = columna
        self.x = columna * ancho + x_inicial
        self.y = fila * ancho
        self.ancho = ancho
        self.total_filas = total_filas
        self.costo = 1
        self.color = (255, 255, 255)
        self.activado = 0

    def getActivado(self):
        """
            Obtener valor de activado
        """
        return self.activado

    def setActivado(self, valor):
        """
            Establecer valor de activado
    	"""
        self.activado = valor

    def getPosicion(self):
        """
            Obtener posición del nodo como una tupla => (fila, columna)		
        """
        return self.fila, self.columna

    def reiniciar(self):
        """
            Poner el nodo en color blanco y desactivarlo.	
        """
        self.color = (255, 255, 255)
        self.setActivado(0)

    def marcarNeurona(self):
        """
            Indicar que el nodo es una neurona (se ha marcado la casilla)	
        """
        self.color = (0, 0, 0)
        self.setActivado(1)

    def dibujar(self, ventana):
        """
            Dibujar el nodo en la ventana.

            Parámetros
        	----------
            ventana: pygame.Surface
	            objeto que representa la ventana para la aplicación.			
        """

        # dibujar el nodo con el color correspondiente (activado -> negro, blanco -> desactivado)
        pygame.draw.rect(ventana, self.color,
                         (self.x, self.y, self.ancho, self.ancho))
