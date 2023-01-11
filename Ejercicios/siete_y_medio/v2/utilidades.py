import random
cartas = [
        ("As♠",1),("2♠",2),("3♠",3),("4♠",4),("5♠",5),("6♠",6),("7♠",7),("10♠",0.5),("11♠",0.5),("12♠",0.5),
        ("As♡ ",1),("2♡ ",2),("3♡ ",3),("4♡ ",4),("5♡ ",5),("6♡ ",6),("7♡ ",7),("10♡ ",0.5),("11♡ ",0.5),("12♡ ",0.5),
        ("As♢",1),("2♢",2),("3♢",3),("4♢",4),("5♢",5),("6♢",6),("7♢",7),("10♢",0.5),("11♢",0.5),("12♢",0.5),
        ("As♣",1),("2♣",2),("3♣",3),("4♣",4),("5♣",5),("6♣",6),("7♣",7),("10♣",0.5),("11♣",0.5),("12♣",0.5)
    ]

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

def imprimeMano(jugador:dict):
    """Imprime las cartas de un jugador.
    las cartas estan en una lista de tuplas :[("As♠",1),("2♠",2)]
    Args:
        jugador (dict): recibe un diccionario que tiene una lista de cartas
    """
    for carta in jugador["cartas"]:
        print(carta[0],end=" ")
    print()