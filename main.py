from lib2to3.pytree import LeafPattern
from juego import Juego
import pygame

ANCHO = 600
LARGO = 1400
ventanaPartida = pygame.display.set_mode((LARGO, ANCHO))

partida = Juego(ventanaPartida, ANCHO, LARGO)
partida.ejecutar()