def bienvenida():
        print('*' * 68)
        print('* BIENVENIDO al Juego de Ahorcado *')
        print('*' * 68)
import random  #Define una serie de funciones para generar o manipular enteros aleatorios.
#Colocamos el dibujo del ahorcado.
dibujo_ahorcado = ['''

   +---+
   |   |
       |
       |
       |
       |u


=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#Creamos el diccionario donde guardaremos nuestra lista de palabras.
diccionario = 'fisica universo programar ciencia animal'.split()
#Buscamos que del diccionario se nos devuelva una palabra al azar, usando lo siguiente:
def obtenerPalabraAlAzar(listaDePalabras):
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]
#Se dibuja el tablero, utilizando 4 palabras, la que muestra el dibujo, donde está la palabra a jugar.
#las que se han adivinado en su posición correcta.
    print(dibujo_ahorcado[len(letrasIncorrectas)])
    print()
#y la lista de letras erróneas para informar al usuario de qué letras han sido utilizadas ya y favorecer que no las repita. 
def mostrarTablero(dibujo_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print('Letras incorrectas:', end=' ') #dejar espacio entre las casillas (salto de línea)
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
 
    espaciosVacíos = '_' * len(palabraSecreta)
 
    for i in range(len(palabraSecreta)): #Encuentran las letras en los espacios vacíos.
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
 
    for letra in espaciosVacíos: #Se observa la palabra adivinar con espacios entre cada letra.
        print(letra, end=' ')
    print()
 
def obtenerIntento(letrasProbadas):
    #Necesitamos realizar un bucle para obtener la letra del usuario, 
    #para solicitársela una y otra vez hasta que introduce una válida.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':  #Comprobamos si se encuentra en esos parámetros, sino se pide de nuevo.
            print('Por favor ingresa una LETRA.')
        else:
            return intento
 
def jugarDeNuevo():
    #Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')
 
print('Bienvenido al juego del A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(diccionario)
juegoTerminado = False
 
while True:
    mostrarTablero(dibujo_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
 
    #Puede el jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
 
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
 
        #Comprueba si el jugador completó la palabra en el tablero, deteniendolo con un break.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Correcto! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Ganaste!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
 
        #Comprobar si se ha cometido el número máximo de errores.
        if len(letrasIncorrectas) == len(dibujo_ahorcado) - 1:
            mostrarTablero(dibujo_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Ya no tienes intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True
 
    #Después de terminar el juego, se pregunta al jugador si quiere volver a jugar.
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(diccionario)
        else:
            break