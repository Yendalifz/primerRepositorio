import random
import art
from jugadorDeSiete import JugadorDeSiete
from carta import Carta
import os
cartas = [
        ("As♠",1),("2♠",2),("3♠",3),("4♠",4),("5♠",5),("6♠",6),("7♠",7),("10♠",0.5),("11♠",0.5),("12♠",0.5),
        ("As♡ ",1),("2♡ ",2),("3♡ ",3),("4♡ ",4),("5♡ ",5),("6♡ ",6),("7♡ ",7),("10♡ ",0.5),("11♡ ",0.5),("12♡ ",0.5),
        ("As♢",1),("2♢",2),("3♢",3),("4♢",4),("5♢",5),("6♢",6),("7♢",7),("10♢",0.5),("11♢",0.5),("12♢",0.5),
        ("As♣",1),("2♣",2),("3♣",3),("4♣",4),("5♣",5),("6♣",6),("7♣",7),("10♣",0.5),("11♣",0.5),("12♣",0.5)
    ]

cartaLista = []
def crear_cartas()->list():
    for carta in cartas:
        cartaLista.append(Carta(carta[0], carta[1]))
    return barajear(cartaLista)

def barajear(cartas:list)->list:
    """ Barajea el maso de cartas
    Args:
        cartas (list)
    Returns:
        list: Retorna el maso de cartas barajeada
    """
    #  guardar cartas barajeadas
    cartas_barajeadas = []
    # barajear
    while(not cartas == []): # mientras no esten vacia
        # agregar en las cartas_barajeadas una carta aleatoria del maso de cartas
        cartas_barajeadas.append(cartas.pop(random.randint(0,len(cartas)-1)))
        
    return cartas_barajeadas

def crearJugador(nombre: str, humano: bool)->dict:
    """Crea aun jugador con nombre,puntos,cartas y si es humano o no.
    Args:
        nombre (str): Nick del jugador
        humano (bool): True si es humano
    Returns:
        dict: con los atribbutos del jugador
    """
    
    jugador = {
        "nombre": nombre,
        "puntos": 0,
        "cartas": [],
        "humano": humano
    }
    return jugador

def imprimeMano(Cartas:list):
    """Imprime las cartas de un jugador.
    las cartas estan en una lista de tuplas :[("As♠",1),("2♠",2)]
    Args:
        jugador (dict): recibe un diccionario que tiene una lista de cartas
    """
    for carta in Cartas:
        print(carta.figura,end=" ")
    print()

def menu(titulo,*opciones,**mensajes):
    while(True):
        os.system('cls')
        arte = art.text2art(titulo,font="tarty2")
        print(arte)
        for i in range(len(opciones)):
            print(f"{i+1}.- {opciones[i]}")
        opt = int(input("Ingresa una opción: "))
        if(0<opt<=len(opciones)):
            return opt
        else:
            print(mensajes["error"])

def crearJugador(humano):
    cpus = ["Deep blue","Polaris","Chinpance","Niño chino"]
    if(humano):
        nick = input("Ingresa tu nick: ")
        return JugadorDeSiete(nick, humano)
    return JugadorDeSiete(cpus[random.randint(0, len(cpus)-1)], humano)