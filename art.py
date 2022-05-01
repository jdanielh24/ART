"""
Archivo: art.py

	Este archivo contiene la clase ART, utilizada para utilizar el algoritmo de Adaptative Resonance Theory.
    Con este algoritmo se puede trabajar con el reconocimiento de patrones.

	Importaciones:
		> numpy: módulo  para crear vectores y matrices grandes multidimensionales, junto con una gran colección 
        de funciones matemáticas de alto nivel para operar con ellas.
"""


import numpy as np


class ART:
    """ 
        Clase ART utilizada para crear una red neuronal utilizando ART.
    """

    def __init__(self, n=4, m=2, pv=.15):
        """
            Inicializar la red con los parámetros correspondientes.

            Parámetros
            -----------
            n : int
                Neuronas de entrada
            m : int
                Neuronas de salida
            pv : float
                Parámetro de vigilancia
        """
        # Capa de comparacion
        self.V1 = np.ones(n)
        # Capa de reconocimiento
        self.V2 = np.ones(m)
        # Pesos de avance
        self.Wf = np.random.random((m,n))
        # Pesos de retroalimentación
        self.Wb = np.random.random((n,m))
        # Vigilancia
        self.pv = pv
        # Número de neuronas activas en V2
        self.activa = 0
    

    def setPv(self, pv):
        """ 
            Establecer self.pv
        
            Parámetros
            ----------
            pv: float
                parámetro de vigilancia
        """
        self.pv = pv


    def aprender(self, X):


        # Calcular la salida V2 y ordenarla)
        self.V2[...] = np.dot(self.Wf, X)
        I = np.argsort(self.V2[:self.activa].ravel())[::-1]

        for i in I:
            # Comprobar si el cálculo es mayor que el parámetro de vigilancia
            d = (self.Wb[:,i]*X).sum()/X.sum()
            if d >= self.pv:
                # Aprender los datos
                self.Wb[:,i] *= X
                self.Wf[i,:] = self.Wb[:,i]/(0.5+self.Wb[:,i].sum())
                return self.Wb[:,i], i

        # No se encontró ninguna coincidencia, aumentar el número de neuronas de salida
        # y hacer que la red aprenda los datos
        if self.activa < self.V2.size:
            i = self.activa
            self.Wb[:,i] *= X
            self.Wf[i,:] = self.Wb[:,i]/(0.5+self.Wb[:,i].sum())
            self.activa += 1
            return self.Wb[:,i], i

        return None,None