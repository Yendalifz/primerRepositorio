import random,palabras,dibujo
class Ahorcado:
    """ Presenta el juego del ahorcado
    """
    def __init__(self) -> str:
        self.__vidas = 6
        
    def __bienvenida(self):
        """Muestra el mensaje de bienvenida
        """
        print('*' * 68)
        print('* BIENVENIDO al Juego de Ahorcado *')
        print('*' * 68)     
        
    def __obtenerPalabraAlAzar(self)->str:
        """Recupera una palabra al azar del diccionario

        Args:
            listaDePalabras (list): una lista de palabras

        Returns:
            str: una palabra al azar
        """
        indiceDePalabras = random.randint(0, len(palabras.lista_palabras) - 1)
        return palabras.lista_palabras[indiceDePalabras]
    
    def __mostrarTablero(self, letrasIncorrectas:str, letrasCorrectas:str, palabraSecreta:str):
        """La variable tablero es una lista ordenada que muestra las líneas de cada letra por adivinar,
        las acertadas y las erroneas.

            Args:
                letrasIncorrectas (list): una lista de palabras contiene todas las letras que ha dicho el jugador. Cuenta los errores, y no se suman las letras repetidas.
                letrasCorrrectas (list): Letras que  adivinó correctamente guardadas.
                palabraSecreta (list): una lista de palabras a adivinar.

            Returns:
                str: letras incorrectas, correctas y la palabra que se usará para adivinar.
        """
        print(dibujo.vidas(self.__vidas-len(letrasIncorrectas)))
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
        
    def __obtenerIntento(self, letrasProbadas:str)->str:
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
            
    def __jugarDeNuevo(self)->str:
        """Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.

        Args: jugarDeNuevo:
            

        Returns: str: Pregunta al usuario si o no juega.
        """
        print('¿Quieres jugar de nuevo? (sí o no)')
        return input().lower().startswith('s')
    
    def inicio(self)->str:
        """Inicia el juego, el usuario introduce una letra.

        Args: 
            

        Returns: str: 'Bienvenido al juego del A H O R C A D O'
        """
        self.__bienvenida()
        letrasIncorrectas = ''
        letrasCorrectas = ''
        palabraSecreta = self.__obtenerPalabraAlAzar()
        juegoTerminado = False
        
        while True:
            self.__mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
        
            #Puede el jugador escribir una letra.
            intento = self.__obtenerIntento(letrasIncorrectas + letrasCorrectas)
        
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
                if len(letrasIncorrectas) == len(dibujo.AHORCADO) - 1:
                    self.__mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
                    print('¡Ya no tienes intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
                    juegoTerminado = True
        
            #Después de terminar el juego, se pregunta al jugador si quiere volver a jugar.
            if juegoTerminado:
                if self.__jugarDeNuevo():
                    letrasIncorrectas = ''
                    letrasCorrectas = ''
                    juegoTerminado = False
                    palabraSecreta = self.__obtenerPalabraAlAzar()
                else:
                    break