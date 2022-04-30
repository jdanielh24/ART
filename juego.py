"""
Archivo: juego.py

	Este archivo contiene la lógica de programación para ejecutar partidas utilizando el algoritmo A-estrella.
	Crea una ventana donde se creará un mapa, una cuadrícula y se podrán seleccionar los nodos de inicio, final
	y obstáculos.

	Importaciones:
		> pygame: módulo que permite la creación de videojuegos en dos dimensiones.
		> tkinter: módulo que provee un conjunto de herramientas GUI.
		> mapa: módulo que se encarga de generar un mapa, en forma de matriz, con una distribución aleatoria de
		los suelos (pasto, bosque, montaña o agua).
		> cuadricula: módulo para crear la cuadrícula que contendrá toda la información de los nodos, además de
		que contiene métodos para dibujar y construir los caminos.
		> a_estrella: módulo que contiene el algoritmo de búsqueda A*.
"""

import pygame
from tkinter import *
from tkinter import messagebox
import cuadricula
import colores as Color
from art import ART
import numpy as np


class Juego:
    """
            Clase utilizada para crear una partida.

            Atributos
    ----------
    DIMENSIONES_POSIBLES : list
            contiene el número de casillas por filas y columnas que una partida puede tener.
                    El mapa más pequeño puede ser de 4x4 y el más grande de 50x50.
    indice_dim : int
            indice para saber cuál valor de DIMENSIONES_POSIBLES se está utilizando.
    """

    DIMENSIONES_POSIBLES = [2, 4, 6, 8, 10, 16, 20, 25, 32, 40, 50]
    indice_dim = 3

    def __init__(self, ventana, ancho, largo):
        """
                Inicializar la ventana para las partidas.

                Parámetros
        ----------
                ventana: game.Surface
                objeto que representa la ventana para la partida.
                ancho: int
                        resolución, en pixeles, que tendrá la ventana.
        """

        self.ventana = ventana
        self.ancho = ancho
        self.largo = largo

        self.ventana.fill(Color.BLANCO)

    def ejecutar(self):
        """
                Este método contiene la lógica y control de las partidas.
        """

        # filas puede ser 4, 6, ... , 40 o 50.
        filas = self.DIMENSIONES_POSIBLES[self.indice_dim]

        # cuadricula_actual es un objeto list con los nodos del mapa ya creados.

        cuadricula_actual = cuadricula.crearCuadricula(filas, self.ancho, 0)

        cuadricula_resultado = cuadricula.crearCuadricula(filas, self.ancho, 800)
        
        red_neuronal = ART(filas*filas, 10, rho=0.4)

        run = True  # para controlar cuándo se detiene la partida

        while run:
            pygame.display.set_caption("Proyecto de IA: ART. Tablero de " + str(self.DIMENSIONES_POSIBLES[self.indice_dim]) + "x" + str(
                self.DIMENSIONES_POSIBLES[self.indice_dim]) + " casillas")  # establecer título de la ventana. Ejemplo: Proyecto IA ... Tablero de 32x32 casillas

            # dibujar la cuadricula, ya con el mapa generado, en la ventana
            cuadricula.dibujar(self.ventana, cuadricula_actual, filas, self.ancho, 0)
            cuadricula.dibujar(self.ventana, cuadricula_resultado, filas, self.ancho, 800)

            # manejo de eventos (acciones con mouse o teclado):
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    # terminar la partida
                    run = False

                if pygame.mouse.get_pressed()[0]:  # click izquierdo
                    posicion = pygame.mouse.get_pos()  # posicion => (x, y)
                    # obtener la fila y columna de la casilla donde se hizo click
                    fila, columna = self.obtenerPosicionDeClick(
                        posicion, filas, self.ancho)
                    
                    if(fila < filas and columna < filas):
                        # nodo seleccionado
                        nodo = cuadricula_actual[fila][columna]
                        nodo.crearBarrera()

                elif pygame.mouse.get_pressed()[2]:  # click derecho
                    posicion = pygame.mouse.get_pos()  # posicion => (x, y)
                    # obtener la fila y columna de la casilla donde se hizo click
                    fila, columna = self.obtenerPosicionDeClick(
                        posicion, filas, self.ancho)
                    # nodo seleccionado
                    nodo = cuadricula_actual[fila][columna]
                    # se resetea el nodo seleccionado, cualquiera que sea su tipo (pasto, bosque, montaña, agua, inicio, fin o obstáculo) se pondrá como nodo de pasto.
                    nodo.reiniciar()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:

                        list = []

                    # recorrer los nodos de cuadricula_actual
                        for fila in cuadricula_actual:
                            for nodo in fila:
                                list.append(nodo.getActivado())
                        
                        arr = np.asarray(list)

                        #print(arr)


                        Z, k = red_neuronal.learn(arr)
                        print("CLASE -> ",k)

                        print(Z.reshape(filas,filas))
                        list_res = self.print_letter(Z.reshape(filas,filas))

                        for fila in range(filas):
                            for columna in range(filas):
                                if list_res[fila][columna] == 1:
                                    nodo = cuadricula_resultado[fila][columna]
                                    nodo.crearBarrera()

                        #print(list_res)

                    # si se presiona alguna de las teclas: [n], [c], [+] ,[-] se actualizará la cuadricula.
                    if evento.key == pygame.K_n or evento.key == pygame.K_c or evento.unicode == "-" or evento.unicode == "+":

                        if evento.key == pygame.K_n or evento.unicode == "-" or evento.unicode == "+":
                            if evento.unicode == "-" or evento.unicode == "+":
                                Tk().wm_withdraw()  # para ocultar la ventana principal que genera Tk
                                if evento.unicode == "-":

                                    if self.indice_dim > 0:  # validar para que no se trate de acceder con indice negativo a DIMENSIONES_POSIBLES
                                        # disminiuir el valor de indice_dim para que apunte a un valor menor de DIMENSIONES_POSIBLES (menor número de casillas)
                                        self.indice_dim -= 1
                                    else:
                                        messagebox.showinfo(
                                            'Advertencia', 'Este es el número mínimo de casillas posibles')
                                        continue
                                if evento.unicode == "+":

                                    # validar para que no se trate de acceder a un indice mayor de los posibles en DIMENSIONES_POSIBLES
                                    if self.indice_dim < len(self.DIMENSIONES_POSIBLES)-1:
                                        # aumentar el valor de indice_dim para que apunte a un valor mayor de DIMENSIONES_POSIBLES (mayor número de casillas)
                                        self.indice_dim += 1
                                    else:
                                        messagebox.showinfo(
                                            'Advertencia', 'Este es el número máximo de casillas posibles')
                                        continue

                            # nuevo número de filas según el cambio en indice_dim
                            filas = self.DIMENSIONES_POSIBLES[self.indice_dim]

                        cuadricula_actual = cuadricula.crearCuadricula(
                            filas, self.ancho, 0)  # actualizar con la nueva cuadricula
                        
                        cuadricula_resultado = cuadricula.crearCuadricula(
                            filas, self.ancho, 800)  # actualizar con la nueva cuadricula

        pygame.quit()  # terminar partida

    def obtenerPosicionDeClick(self, posicion, filas, ancho):
        """
                Obtener la posición del nodo, (fila, columna), donde se hizo click en la cuadrícula.

                Parámetros
        ----------
                posicion: tuple
                contiene la posición del pixel donde se hizo click => (x, y)
                filas: int
                        número de filas que contiene la cuadrícula actual. Es uno de los valores de DIMENSIONES_POSIBLES.
                ancho: int
                        tamaño, en píxeles, de la ventana de la partida.
        """

        anchoCasilla = ancho // filas
        x, y = posicion

        fila = y // anchoCasilla
        columna = x // anchoCasilla

        return fila, columna
       
    def print_letter(self, Z):
        ''' Print an array as if it was a letter'''
        lst = []
        for row in range(Z.shape[0]):
            lst.append([])
            for col in range(Z.shape[1]):
                if Z[row,col]:
                    lst[row].append(1)
                else:
                    lst[row].append(0)
        return lst