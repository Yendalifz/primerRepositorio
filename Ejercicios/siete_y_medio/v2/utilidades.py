import random
cartas = [
        ("As♠",1),("2♠",2),("3♠",3),("4♠",4),("5♠",5),("6♠",6),("7♠",7),("10♠",0.5),("11♠",0.5),("12♠",0.5),
        ("As♡ ",1),("2♡ ",2),("3♡ ",3),("4♡ ",4),("5♡ ",5),("6♡ ",6),("7♡ ",7),("10♡ ",0.5),("11♡ ",0.5),("12♡ ",0.5),
        ("As♢",1),("2♢",2),("3♢",3),("4♢",4),("5♢",5),("6♢",6),("7♢",7),("10♢",0.5),("11♢",0.5),("12♢",0.5),
        ("As♣",1),("2♣",2),("3♣",3),("4♣",4),("5♣",5),("6♣",6),("7♣",7),("10♣",0.5),("11♣",0.5),("12♣",0.5)
    ]

def barajear()->list:
    """_barajear_
        barajea el maso con la función random.randint
    Returns:
        list: retorna el maso de cartas barajeada
    """
    #  guardar cartas barajeadas
    cartas_barajeadas = []
    # barajear
    while(not cartas == []): # mientras no esten vacia
        # agregar en las cartas_barajeadas una carta aleatoria del maso de cartas
        cartas_barajeadas.append(cartas.pop(random.randint(0,len(cartas)-1)))
        
    return cartas_barajeadas
