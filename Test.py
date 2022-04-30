import numpy as np

class RedNeuronal:
    #n = neuronas de entrada
    #m = neuronas de salida
    #p = nivel de semejanza
    def __init__(self, n, m, p):
        self.n = n
        self.m = m
        self.p = p
        #ones regresa una matriz llena de unos con la dimension que especifiquemos
        self.comparacion = np.ones(n)
        self.reconocimiento = np.ones(m)
        #matriz de aprendizaje
        #random crea numeros aleatorios con los limites dados
        self.v = np.random.random(m,n)
        #matriz de neuronas
        self.w = np.random.random((n,m))
        self.neuronasDeReconocimiento = 0

       
    #X es la matriz que recibimos del usuario
    def aprendizaje(self, X): 
        #dot calcula el producto escalar de dos matrices
        self.reconocimiento[...] = np.dot(self.v, X)
        #con argsort obtenemos los indices de la matriz de forma ordenada
        #Ravel nos devuelve una matriz de una dimension y a gregamos ::-1 para hacerlo de forma inversa
        matrizOrdenada = np.argsort(self.reconocimiento[:self.neuronasDeReconocimiento].ravel())[::-1]

        for i in matrizOrdenada:
            #Comprobamos si el valor es mayor al nivel de semejanza

            #Calculo de la neurona para la formula de la competencia
            d = (self.w[:i]*X).sum()/X.sum()
            #la neurona es mayor o igual al nivel de semejanza
            if d >= self.p:
                #Encontramos el patron
                self.w[:,i] *= X
                #actualizamos la matriz de pesos
                #Formula de actualizacion de pesos
                self.v[i,:] = self.w[:,i]/(0.5+self.w[:,i].sum())
                #regresamos la matriz de neuronas 
                return self.w[:,i], i

            #Si el patron ingresado no existe, agregamos las neuronas de reconocimiento para 
            #identificarlo la siguiente vez
            if self.neuronasDeReconocimiento < self.reconocimiento.size:
                i = self.neuronasDeReconocimiento
                self.w[:,i] *= X
                #Formula de actualizacion de pesos
                self.v[i,:] = self.w[:,i]/(0.5+self.w[:,i].sum())
                self.neuronasDeReconocimiento += 1
                return self.w[:,i], i

            return None, None

if __name__ == '__main__':
    n = 4
    m = 2
    p = 0.8
    redneuronal = RedNeuronal(n,m,p)
    datos = [   "1100", #E1
                "0011", #E3 
                "1110"] #E3

#creamos una matriz de ceros con la dimension de la matriz de datos
X = np.zeros(len(datos[0]))

#recorremos la matriz
for i in range(len(datos)):
    for j in range(len(datos[i])):
        X[j] = (datos[i][j] == '0')
        Z, k = redneuronal.aprendizaje(X)
        print("|%s|"%datos[i],"-> pertenece a la clase ", k)


#######################################################

""""














    #n = 4
    #m = 2
    #p = 0.8
    #estabilizador_gamma = 0.5
    #v = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     #    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        
    valorW = round(1/(1+n), 2)
   
   #funcion que crea una matriz de 1 con dos dimensiones y multiplicarlo por los valores reales
    def matriz_de_1(n, m):
        matriz = []
        for i in range(n):
            matriz.append([])
            for j in range(m):
                matriz[i].append(1)
        return matriz
  
 

 
   
    #creacion de matrices
    #matrize de v= 2,16, y w 16,2
    v = matriz_de_1(2,4)
    w = matriz_de_1(4,2)
    #Patron de ejemplo para pruebas 
    e1 = [1,1,0,0]
    e2 = [0,0,1,1]
    e3 = [1,1,1,0]
    #funcion que convierte una matriz a vector
    def matriz_a_vector(matriz):
        vector = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                vector.append(matriz[i][j])
        return vector

    #funcion que multiplica una matriz por un escalar
    def escalar(matriz, escalar):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = escalar*matriz[i][j]
        return matriz
    
    #funcion que sustituye una fila de una matriz por un vector
    def sustitucion(matriz, vector, fila):
        for i in range(len(vector)):
            matriz[fila][i] = vector[i]
        return matriz
    
    
    #entrada_usuario = (matriz_a_vector(entrada_usuario))
    v = sustitucion(v, e1,0)
    w = escalar(w, valorW)
   
   #neuronas de salida
    ns1 = 0.0
    ns2 = 0.0
    #por default la neurona ns1 es la vencedora al ser la primera neurona y no haber informacion

    #Funcion que calcula el peso w de la neurona de salida utlizando la furmoula Wj*i(t+1)
    def calculo_w(entrada_usuario,v, w, gamma):
        for i in range(len(v)):
            for j in range(len(w)):
                w[j][i] = round (v[i][j]*entrada_usuario[i] / (gamma+v[i][j])*entrada_usuario[i], 2)
        return w
       

    #funcion que realiza una operacion AND entre las files de una matriz
    def AND(matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 1:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
        return matriz
    resultadoAND = AND(v)


    #print(calculo_w(e1,v,w,estabilizador_gamma))
"""