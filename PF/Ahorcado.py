import random  #Define una serie de funciones para generar o manipular enteros aleatorios.
#Colocamos el dibujo del ahorcado.
import dibujo as d
import Palabras as p

diccionario = p.lis

#class Ahorcado(Juego): DUDA
    
    #def __init__(self):
        #d.__init__(self,"Ahorcado")
        #0self.__dibujo = []
        #self.__baraja = utl.crear_cartas()

def bienvenida():
    """Muestra el mensaje de bienvenida
    """
    print('*' * 68)
    print('* BIENVENIDO al Juego de Ahorcado *')
    print('*' * 68)
#Creamos el diccionario donde guardaremos nuestra lista de palabras.
#Buscamos que del diccionario se nos devuelva una palabra al azar, usando lo siguiente:
def obtenerPalabraAlAzar(listaDePalabras:list)->str:
    """Recupera una palabra al azar del diccionario

    Args:
        listaDePalabras (list): una lista de palabras

    Returns:
        str: una palabra al azar
    """
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]
#y la lista de letras erróneas para informar al usuario de qué letras han sido utilizadas ya y favorecer que no las repita. 
def mostrarTablero(letrasIncorrectas:list, letrasCorrectas:list, palabraSecreta:list)->str:
  """La variable tablero es una lista ordenada que muestra las líneas de cada letra por adivinar,
  las acertadas y las erroneas.

    Args:
        letrasIncorrectas (list): una lista de palabras contiene todas las letras que ha dicho el jugador. Cuenta los errores, y no se suman las letras repetidas.
        letrasCorrrectas (list): Letras que  adivinó correctamente guardadas.
        palabraSecreta (list): una lista de palabras a adivinar.

    Returns:
        str: letras incorrectas, correctas y la palabra que se usará para adivinar.
    """
    print(d.vidas(6-len(letrasIncorrectas)))
    print('Letras incorrectas:', end=' ') # dejar espacio entre las casillas (salto de línea)
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
 
def obtenerIntento(letrasProbadas)->str:
    """Necesitamos realizar un bucle para obtener la letra del usuario, 
    para solicitársela una y otra vez hasta que introduce una válida.
    si la letra es repetida también tenemos que volver a solicitar una letra al usuario.

    Args: letrasProbadas (list): lista de letras usadas.
        

    Returns: str: Las letras que utilizas para adivinar.
    """
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
def jugarDeNuevo()->str:
    """Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.

    Args: jugarDeNuevo:
        

    Returns: str: Pregunta al usuario si o no juega.
    """
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')
 
def inicio()->str:
    """Inicia el juego, el usuario introduce una letra.

    Args: 
        

    Returns: str: 'Bienvenido al juego del A H O R C A D O'
    """
    print('Bienvenido al juego del A H O R C A D O')
    letrasIncorrectas = ''
    letrasCorrectas = ''
    palabraSecreta = obtenerPalabraAlAzar(diccionario)
    juegoTerminado = False
    
    while True:
        mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
    
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
            if len(letrasIncorrectas) == len(d.AHORCADO) - 1:
                mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
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

        