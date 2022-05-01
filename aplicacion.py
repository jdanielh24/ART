"""
Archivo: Aplicacion.py

	Este archivo contiene la lógica de programación para ejecutar la aplicación utilizando ART para el
    reconocimiento de patrones. Crea una ventana donde se crearán dos cuadrículas:
        > cuadricula izquierda: se puede ingresar un nuevo patrón al hacer click en las casillas.
        > cuadrícula derecha: se muestra el patrón reconocido.
    También se puede cambiar el parámetro e viligancia a través de un InputText.

	Importaciones:
		> pygame: módulo que permite la creación de videojuegos en dos dimensiones.
		> cuadricula: módulo para crear la cuadrícula que contendrá toda la información de los nodos (casillas). 
		> numpy: módulo  para crear vectores y matrices grandes multidimensionales, junto con una gran colección 
        de funciones matemáticas de alto nivel para operar con ellas.
        > art: módulo para crear una red neuronal y entrenarla con ART para el reconocimiento de patrones.
        > tkinter: módulo que provee un conjunto de herramientas GUI.
        > inputText: módulo que permite crear un campo de datos de entrada.
"""

import pygame
import cuadricula
import numpy as np
from art import ART
from tkinter import *
from tkinter import messagebox
from inputText import InputBox

class Aplicacion:
    """
        Clase utilizada para crear la aplicación.

        Atributos
        ----------
        DIMENSIONES_POSIBLES : list
            contiene el número de casillas por filas y columnas que una cuadrícula puede tener.
            La cuadrícula más pequeña puede ser de 2x2 y la más grande de 16x16.
        indice_dim : int
            indice para saber cuál valor de DIMENSIONES_POSIBLES se está utilizando.
    """

    DIMENSIONES_POSIBLES = [2, 4, 6, 8, 10, 16]
    indice_dim = 4

    def __init__(self):
        """
            Inicializar la ventana para la aplicación.

            Atributos
            ----------
            ancho: int
                ancho de laresolución, en pixeles, que tendrá la ventana.
            largo: int
                largo de la resolución, en pixeles, que tendrá la ventana.    
            ventana: game.Surface
                objeto que representa la ventana para la partida.   
        """

        self.ancho = 600
        self.largo = 1400
        self.ventana = pygame.display.set_mode((self.largo, self.ancho))
        self.ventana.fill((255, 255, 255)) # poner el fondo en blanco

        pygame.display.set_caption("Proyecto de IA: ART. " )  # establecer título de la ventana

    def ejecutar(self):
        """
            Este método contiene la lógica y control de la aplicación.
        """

        # filas, puede ser 2, 4, ... , o 16
        filas = self.DIMENSIONES_POSIBLES[self.indice_dim]

        par_vigilancia = 0.8 # parámetro de vigilancia inicial

        self.input_box1 = InputBox(630, 100, 140, 32, pv=par_vigilancia) # crear InputText

        # cuadrícula de la izquierda, donde se puede dibujar un patrón
        cuadricula_dibujo = cuadricula.crearCuadricula(filas, self.ancho, 0)

        # cuadrícula de la derecha, donde se puede ver el patrón reconocido
        cuadricula_resultado = cuadricula.crearCuadricula(filas, self.ancho, 800)

        neuronas_salida = 16 # neuronas de salida por default

        # crear red neuronal
        red_neuronal = ART(filas*filas, neuronas_salida, pv=par_vigilancia)

        clase = "" # variable para almacenar la clase a la que pertenece el patrón

        run = True  # para controlar cuándo se detiene la partida

        while run:

            self.agregarEtiquetas(filas, par_vigilancia, clase)

            par_vig_aux = self.input_box1.getPV() # obtener pv del input text

            # actualiza pv solo si es introducido un nuevo valor
            if (par_vigilancia != par_vig_aux):
                par_vigilancia = par_vig_aux
                red_neuronal.setPv(par_vigilancia)

            # dibujar las cuadriculas
            cuadricula.dibujar(self.ventana, cuadricula_dibujo, filas, self.ancho, 0)
            cuadricula.dibujar(self.ventana, cuadricula_resultado, filas, self.ancho, 800)

            # manejo de eventos (acciones con mouse o teclado):
            for evento in pygame.event.get():
                self.input_box1.manejar_evento(evento)
                if evento.type == pygame.QUIT:
                    # terminar la partida
                    run = False

                if pygame.mouse.get_pressed()[0]:  # click izquierdo
                    posicion = pygame.mouse.get_pos()  # posicion => (x, y)
                    # obtener la fila y columna de la casilla donde se hizo click
                    fila, columna = self.obtenerPosicionDeClick(posicion, filas, self.ancho)

                    # si se presiona en una casilla de la cuadrícula de la izquierda...
                    if (fila < filas and columna < filas):
                        nodo = cuadricula_dibujo[fila][columna] # nodo seleccionado
                        nodo.marcarNeurona() # poner casilla de color negro

                elif pygame.mouse.get_pressed()[2]:  # click derecho
                    posicion = pygame.mouse.get_pos()  # posicion => (x, y)
                    # obtener la fila y columna de la casilla donde se hizo click
                    fila, columna = self.obtenerPosicionDeClick(posicion, filas, self.ancho)

                    # si se presiona en una casilla de la cuadrícula de la izquierda:
                    if (fila < filas and columna < filas):                        
                        nodo = cuadricula_dibujo[fila][columna] # nodo seleccionado
                        nodo.reiniciar() # poner casilla de color blanco

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE: # si se presiona tecla de espacio

                        lista = [] # contendrá el patrón reconocido

                        # recorrer los nodos de cuadricula_dibujo
                        for fila in cuadricula_dibujo:
                            for nodo in fila:
                                lista.append(nodo.getActivado()) # agregar si está activado o no

                        arr = np.asarray(lista) # convertir lista a objeto ndarray


                        Z, k = red_neuronal.aprender(arr) # aprender patrón
                        clase = k # indicar la clase a la que pertener el patrón

                        lista_res = self.getPatron(Z.reshape(filas, filas)) # obtener el patrón en objeto list
                        
                        # recorrer la lista con el patrón reconocido para dibujarlo en la cuadricula derecha
                        for fila in range(filas):
                            for columna in range(filas):
                                if lista_res[fila][columna] == 1:
                                    nodo = cuadricula_resultado[fila][columna]
                                    nodo.marcarNeurona()
                        cuadricula.dibujar(self.ventana, cuadricula_resultado, filas, self.ancho, 800)

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

                            # crear nueva red neuronal si se presiona [n], [+] o [-]
                            red_neuronal = ART(filas*filas, neuronas_salida, pv=par_vigilancia)

                            Tk().wm_withdraw()  # para ocultar la ventana principal que genera Tk
                            messagebox.showinfo( 'Importante', 'Se creó una nueva red neuronal')
                            clase = ""

                        # actualizar nuevas cuadriculas
                        cuadricula_dibujo = cuadricula.crearCuadricula(filas, self.ancho, 0)  

                        cuadricula_resultado = cuadricula.crearCuadricula(filas, self.ancho, 800)  

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
                tamaño, en píxeles, de la cuadrícula donde se dibujar.
        """

        anchoCasilla = ancho // filas
        x, y = posicion

        fila = y // anchoCasilla
        columna = x // anchoCasilla

        return fila, columna

    def getPatron(self, Z):
        """ 
            Guardar Z en un objeto list

            Parametros
            ----------
            Z: ndarray
                Objeto que contiene un patrón
        """
        lst = []
        for fila in range(Z.shape[0]):
            lst.append([])
            for columna in range(Z.shape[1]):
                if Z[fila, columna]:
                    lst[fila].append(1)
                else:
                    lst[fila].append(0)
        return lst

    def agregarEtiquetas(self, filas, par_vigilancia, clase=""):
        """
            Agregar las etiquetas de información en la ventana

            Parámetros
            ----------
            filas: int
                número de filas que contiene la cuadrícula actual. Es uno de los valores de DIMENSIONES_POSIBLES.
            par_vigilancia: int
                parámetro de vigilancia para la red neurona
            clase: int
                clase a la que pertenece el patrón
        """
        
        # dibujar area del medio de la ventana
        pygame.draw.rect(self.ventana, (255, 255, 255), (600, 0, 200, self.largo))
        self.input_box1.dibujar(self.ventana) # agregar el InputText

       # crear texto, obtener un objeto Rect de él y almacenarlo en un contenedor:
        self.textoPV = pygame.font.Font(None, 20).render("Parámetro de vigilancia: " + str(par_vigilancia), True, pygame.Color('dodgerblue2'))
        # center=(x,y) => centrar en dicha posicion.
        contenedorTextoPV = self.textoPV.get_rect(center=(700, 80))
        self.ventana.blit(self.textoPV, contenedorTextoPV)

        self.textoNE = pygame.font.Font(None, 20).render("Neuronas de entrada: " + str(filas * filas), True, pygame.Color('dodgerblue2'))
        contenedorTextoNE = self.textoNE.get_rect(center=(700, 20))
        self.ventana.blit(self.textoNE, contenedorTextoNE)

        self.textoClase = pygame.font.Font(None, 20).render("Clase a la que pertenece: " + str(clase), True, pygame.Color('dodgerblue2'))
        contenedorTextoClase = self.textoClase.get_rect(center=(700, 230))
        self.ventana.blit(self.textoClase, contenedorTextoClase)

        self.textoControles = pygame.font.Font(None, 20).render("Controles: ", True, pygame.Color('dodgerblue2'))
        contenedorTextoControles = self.textoControles.get_rect(center=(700, 360))
        self.ventana.blit(self.textoControles, contenedorTextoControles)

        self.textoClickDer = pygame.font.Font(None, 20).render("Marcar casilla: Click derecho", True, pygame.Color('dodgerblue2'))
        contenedorTextoClickDer = self.textoClickDer.get_rect(center=(700, 400))
        self.ventana.blit(self.textoClickDer, contenedorTextoClickDer)

        self.textoClickIzq = pygame.font.Font(None, 20).render("Desmarcar casilla: Click izq.", True, pygame.Color('dodgerblue2'))
        contenedorTextoClickIzq = self.textoClickIzq.get_rect(center=(700, 430))
        self.ventana.blit(self.textoClickIzq, contenedorTextoClickIzq)

        self.textoEspacio = pygame.font.Font(None, 20).render("Guardar patrón: [espacio]", True, pygame.Color('dodgerblue2'))
        contenedorTextoEspacio = self.textoEspacio.get_rect(center=(700, 460))
        self.ventana.blit(self.textoEspacio, contenedorTextoEspacio)

        self.textoEspacio = pygame.font.Font(None, 20).render("Limpiar patrón: [c]", True, pygame.Color('dodgerblue2'))
        contenedorTextoLimpiar = self.textoEspacio.get_rect(center=(700, 490))
        self.ventana.blit(self.textoEspacio, contenedorTextoLimpiar)

        self.textoNueva = pygame.font.Font(None, 20).render("Nueva red neuronal: [n]", True, pygame.Color('dodgerblue2'))
        contenedorTextoNueva = self.textoNueva.get_rect(center=(700, 520))
        self.ventana.blit(self.textoNueva, contenedorTextoNueva)