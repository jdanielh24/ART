"""
Archivo: nodo.py

	Este archivo contiene la clase Nodo, utilizada para almacenar los atributos de cada casilla en la cuadrícula
	(tipo, color, costos, posición, vecinos etc).

	Importaciones:
		> pygame: módulo que permite la creación de videojuegos en dos dimensiones.
		> módulo que provee un conjunto de diferentes colores en formato RGB.
"""

import pygame
import colores as Color

pygame.init()  # si se omite, no se crearán las fuentes. Se necesitan inicializar

# crear fuentes con distintos tamaños
FONT_12 = pygame.font.SysFont('chalkduster.ttf', 12)
FONT_18 = pygame.font.SysFont('chalkduster.ttf', 18)
FONT_32 = pygame.font.SysFont('chalkduster.ttf', 32)


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
                fila en que se encuentra el nodo
                columna: int
                        columna en que se encuentra el nodo
                ancho: int
                ancho de la casilla del nodo
                total_filas: int
                        numero de filas que hay en la cuadricula donde se encuentra el nodo.

                Otros atributos
        ----------
                x: int
                posicion en el eje X donde se encuentra el nodo
                y: int
                        posicion en el eje Y donde se encuentra el nodo
                vecinos: list
                vecinos del nodo
                costo: int
                        costo que cuesta moverse por ese nodo, dependiendo del tipo de suelo. Es utilizado para calcular G en a_estrella.py
                f: str / int	
                        valor de f. Es utilizadoo en a_estrella.py para determinar el camino más corto.
                final: bool
                        True si es el nodo de fin (objetivo), de lo contrario es False.
        """
        self.fila = fila
        self.columna = columna
        self.x = columna * ancho + x_inicial
        self.y = fila * ancho
        self.vecinos = []
        self.ancho = ancho
        self.total_filas = total_filas
        self.costo = 1
        self.color = Color.BLANCO
        self.activado = 0

    def getActivado(self):
        return self.activado
    
    def setActivado(self, valor):
        self.activado = valor

    def getCosto(self):
        """
                Obtener valor de costo		
        """
        return self.costo

    def getPosicion(self):
        """
                Obtener posición del nodo como una tupla => (fila, columna)		
        """
        return self.fila, self.columna

    def reiniciar(self):
        """
                Indicar que el nodo es pasto	
        """
        self.color = Color.BLANCO
        self.setActivado(0)

    def crearBarrera(self):
        """
                Indicar que el nodo es una barrera	
        """
        self.color = Color.NEGRO
        self.setActivado(1)

    def dibujar(self, ventana):
        """
                dibujar el nodo en la ventana.

                Parámetros
        ----------
                ventana: pygame.Surface
                objeto que representa la ventana para la partida.			
        """

        # dibujar el nodo con el color de acuerdo al tipo de suelo o si es de inicio, fin o barrera
        pygame.draw.rect(ventana, self.color,
                         (self.x, self.y, self.ancho, self.ancho))
