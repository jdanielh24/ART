"""
Archivo: cuadricula.py

	Contiene funciones para crear y dibujar una cuadrícula, en la que cada casilla será un objeto Nodo. 

	Importacioness:
		> nodo: módulo que provee objetos del tipo Nodo, para almacenar todo su información (si está activado o no).
		> pygame: módulo que permite la creación de videojuegos en dos dimensiones.
"""

from nodo import Nodo
import pygame

def crearCuadricula(filas, ancho, x_inicial):
	"""
		Crea un objeto list que representa la cuadrícula, la cuál está conformada por casillas, donde cada una es un Nodo.

		Parámetros
   		----------
		filas: int
	   		número de filas (y columnas) que debe de tener la cuadricula.
		ancho: int
	   		ancho (y alto) de toda la cuadrícula (# de pixeles).
		x_inicial: int
	   		valor inicial de la coordenada x.		   	
	"""	

	cuadricula = []
	anchoCasilla = ancho // filas # obtener la medida de cada casilla

	for i in range(filas):
		cuadricula.append([])
		for j in range(filas):
			nodo = Nodo(i, j, anchoCasilla, filas, x_inicial) # crear Nodo para el objeto cuadricula[i][j]
			
			cuadricula[i].append(nodo) # agregar el nodo en cuadricula

	return cuadricula


def dibujarCuadricula(ventana, filas, ancho, x_inicial):
	"""
		Se dibujan las rayas verticales y horizontales en la ventana, las cuales sirven para hacer las divisiones entre casillas.

		Parámetros
   		----------
		ventana: pygame.Surface
	   		objeto que representa la ventana para la partida.
		filas: int
	   		número de filas (y columnas) que debe de tener la cuadricula.
		ancho: int
	   		ancho (y alto) de toda la cuadrícula (# de pixeles).
		x_inicial: int
	   		valor inicial de la coordenada x.	
	"""
	anchoCasilla = ancho // filas
	
	for i in range(filas):
		pygame.draw.line(ventana,(128, 128, 128), (x_inicial, i * anchoCasilla), (ancho + x_inicial , i * anchoCasilla)) # rayas horizontales
		for j in range(filas+1):
			pygame.draw.line(ventana, (128, 128, 128), ((j * anchoCasilla) + x_inicial, 0), ((j * anchoCasilla) + x_inicial, ancho)) # rayas verticales

def dibujar(ventana, cuadricula, filas, ancho, x_inicial):
	"""
		Se dibuja la cuadricula en la ventana.
		La cuadricula ya contiene los nodos con su respectiva información (ej: si está activado o no)

		Parámetros
   		----------
		ventana: pygame.Surface
	   		objeto que representa la ventana para la aplicacion.
		cuadricula: list
			contiene todos los nodos que conforman la cuadricula.
		filas: int
	   		número de filas (y columnas) que debe de tener la cuadricula.
		ancho: int
	   		ancho (y alto) de toda la cuadrícula (# de pixeles).
		x_inicial: int
	   		valor inicial de la coordenada x.		
	"""
	for fila in cuadricula:
		for nodo in fila:
			nodo.dibujar(ventana) # se dibuja el nodo en cuestión (cambia el tipo de color, el margen, el costo mostrado, etc)

	dibujarCuadricula(ventana, filas, ancho, x_inicial)
	pygame.display.update()
