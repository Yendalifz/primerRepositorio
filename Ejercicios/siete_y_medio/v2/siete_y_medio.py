import random
import time
import utilidades as utl
# tosn
def pedirCarta() -> tuple:
    """Pide una carta del maso de cartas barajeadas
    Returns:
        tuple: una carta con (figura,valor)
    """
    return cartas_barajeadas.pop()


def iniciar():
    """Inicia el juego.
    Crea a los jugadores y muestra quien gano.
    """
    cartas_barajeadas = utl.barajear()
    nombre = input("Ingresa tu nombre: ")
    jugador1 = utl.crearJugador(nombre, True)
    jugador2 = utl.crearJugador("Polaris", False)
    ganador = inicia_el_juego(jugador1, jugador2)
    if(ganador.get("nombre","no hay ganador")!="no hay ganador"):
        print("El ganador es",ganador["nombre"])
    else:
        print(ganador["mensaje"])

def inicia_el_juego(jugador1, jugador2) -> dict:
    """Los jugadores comienzan a pedir cartas.
    Args:
        jugador1 (_type_)
        jugador2 (_type_)
    Returns:
        dict: El diccionario es un jugador o un diccionario con un mensaje {"mensaje":mensaje}
    """
    jugar(jugador1)
    jugar(jugador2)
    return verificaGanador(jugador1, jugador2)


def jugar(jugador: dict):
    """Los jugadores pueden pedir cartas.
    Args:
        jugador (dict)
    """
    nombre = jugador["nombre"]
    primera_carta = True
    jugar = True
    while (jugar):
        if (not primera_carta):
            utl.imprimeMano(jugador)
            if (jugador["humano"] and regla(jugador) and int(input(f"{nombre}: quieres otra carta si:1 no:0 - "))):
                ronda(jugador)
            elif (not jugador["humano"] and regla(jugador)):
                jugar = rondaCPU(jugador)
            else:
                jugar = False
        else:
            ronda(jugador)
            primera_carta = False

def ronda(jugador: dict):
    """El jugador toma una carta. y acumula puntos.
    Args:
        jugador (dict): tiene que tomar la decisión ( no cpu).
    """
    print("Turno:", jugador["nombre"])
    carta = pedirCarta()
    jugador["cartas"].append(carta)
    jugador["puntos"] += carta[1]

def rondaCPU(jugador: dict) -> bool:
    """juega una ronda al azar.
    Decide si quiere pedir más cartas con números pseudoaleatorios.
    Args:
        jugador (dict): tiene que ser cpu.
    Returns:
        bool: si quere seguir jugando o no.
    """
    pedir = random.random() >= 0.5
    mnj = "si" if pedir else "no"
    print("quieres otra carta?")
    print(f"{mnj}")
    if (pedir):
        time.sleep(2)
        ronda(jugador)
        return True
    return False

def verificaGanador(jugador1: dict, jugador2: dict) -> dict:
    """Verifica que jugador gano, si empataron o si nadie gano.
    Args:
        jugador1 (dict): tiene que tener la llave puntos.
        jugador2 (dict): '''.
    Returns:
        dict: retorna el jugador ganador, en case de empate un dict("mensaje":mensaje).
    """
    nombre1 = jugador1["nombre"]
    nombre2 = jugador2["nombre"]
    if (regla(jugador1) and regla(jugador2)):
        if (jugador1['puntos'] == jugador2['puntos']):
            return {"mensaje": "Empate"}
        elif (jugador1['puntos'] < jugador2['puntos']):
            return jugador2
        else:
            return jugador1
    elif (not regla(jugador1) and not regla(jugador2)):
        return {"mensaje": "Ninguno gana"}
    else:
        return jugador1 if regla(jugador1) else jugador2

def regla(jugador: dict) -> bool:
    """La regla del juego 7 y 1/2 es no pasarse de 7.5 puntos.
    Args:
        jugador (dict): el jugador tiene que tener la clave de puntos.
    Returns:
        bool: si cumple la regla o no.
    """
    return jugador["puntos"] <= 7.5

iniciar()
