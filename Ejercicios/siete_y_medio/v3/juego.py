from jugador import Jugador
class Juego:

    def __init__(self,nombre:str):
        self.__nombre = nombre # los juegos tienen un nombre

    def inicio(self):
        """Inicia el juego
        """
        print(self.__nombre)

    def __reglas(self):
        """Reglas del juego, estas reglas las tiene que cumplir el jugador para
        no perder.
        """
        pass
    
    def __terminar(self):
        """Verifica cuando tiene que terminar el juego
        """
        pass


    # getters y setters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre