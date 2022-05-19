# ART

La teoría de la resonancia adaptativa (en inglés, adaptive resonance theory, conocido por sus siglas inglesas ART), desarrollada por Stephen Grossberg y Gail Carpenter. Es un modelo de red neuronal artificial (RNA) que basa su funcionamiento en la manera en que el cerebro procesa información y que describe una serie de modelos de redes neuronales que utilizando métodos de aprendizaje supervisado y no supervisado abordan problemas tales como el reconocimiento y la predicción de patrones.

## Características del ART
- El aprendizaje se produce mediante un mecanismo de realimentación creado por la competencia entre las neuronas de la capa de salida y la capa de entrada de la red.
- El aprendizaje es no supervisado, aunque existe una modalidad supervisada.
- La red crea su propia clasificación de lo que aprende.

## Arquitectura del ART

Es una red formada por dos capas:
- Capa de entrada (F1): datos de entrada pasan a ser los valores de sus neuronas, en ella también se hace la comparación de similitud.
- Capa de salida (F2): es una capa de neuronas competitivas, o sea todas compiten para ser la ganadora, pero solo una puede ser la ganadora y esta inhibe a las demás.
- Parámetro de vigilancia (p): Dice cuan semejante debe ser la entrada con la categoría seleccionada. Este parámetro está dado por 0 < x > 1, si "x" es muy cercano a 0, muchas entradas serán categorizadas en una misma categoría, mientras si "x" en muy cercano a 1 se crearán muchas categorías (memorización)
- Sistema de orientación: Sirve para orientar la red, ya que las neuronas de ambas capas están totalmente interconectadas y hay una afluencia hacia adelante y hacia atrás.
- Sistema de reinicio: Sirve para inhibir la neurona ganadora cuando dicha no cumple con la vigilancia, en el proceso de comparación de similitud.

## Aplicación
Esta aplicación, cuenta con dos cuadrículas de n x n casillas, donde n x n = número de neuronas de entrada:
- Primera cuadrícula: El usuario podrá dibujar un patrón al hacer click en cualquiera de las casillas de la cuadrícula.
- Segunda cuadrícula: Aquí se mostrará el patrón reconocido por la red neuronal. 

Una vez que se introduzca un patrón, el usuario podrá presionar un botón para que este sea guardado en la red y que se realice el entrenamiento de la misma. Posteriormente, el patrón que sea reconocido por la red, será visible al usuario.	 

En cuanto al parámetro de vigilancia, el usuario podrá modificarlo, introduciendo un valor, entre 0 y 1, en un campo de entrada de texto.


## Requisitos
Python +3.0

Instalar PyGame: 

```pip install pygame```

## Ejecución
Acceder a la ruta donde se encuentra el proyecto y ejecutar el comando:

```python main.py```

## Pruebas
