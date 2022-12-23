import functools as f
from jugador import Jugador
from carta import Carta
import random as r
import time
class JugadorDeSiete(Jugador):
    def __init__(self,nick:str,humano:bool):
        Jugador.__init__(self,nick)
        self.__puntos = 0.0
        self.__mano_de_cartas = []
        self.__humano = humano
    
    def pedir_carta(self,carta:Carta):
        self.__mano_de_cartas.append(carta)
    
    def calcular_puntos(self):
        self.__puntos = f.reduce(self.__sumar_puntos, self.__mano_de_cartas, 0)
        return self.__puntos
    
    def __sumar_puntos(self,puntos:float,carta:Carta):
        return puntos+carta.valor
    
    def seguir_jugando(self,pregunta:str):
        if(self.__humano):
            return True if int(input(pregunta)) else False
        else:
            print(pregunta)
            time.sleep(3)
            respuesta = "si" if r.random()>0.5 else "no"
            print(respuesta)
            time.sleep(3)
            return True if respuesta=="si" else False

    def reiniciar(self):
        self.__puntos = 0.0
        self.__mano_de_cartas = []

    def __str__(self):
        return f"{self.nick} : {self.puntos}"
    # getters y setters
    @property
    def puntos(self):
        return self.__puntos
    
    @puntos.setter
    def puntos(self,puntos):
        self.__puntos = puntos
    
    @property
    def mano_de_cartas(self):
        return self.__mano_de_cartas
    
    @mano_de_cartas.setter
    def mano_de_cartas(self,mano_de_cartas):
        self.__mano_de_cartas = mano_de_cartas
    
    @property
    def humano(self):
        return self.__humano