import random,time

# Creación de una lista de tuplas.
cartas = [
        ("As♠",1),("2♠",2),("3♠",3),("4♠",4),("5♠",5),("6♠",6),("7♠",7),("10♠",0.5),("11♠",0.5),("12♠",0.5),
        ("As♡ ",1),("2♡ ",2),("3♡ ",3),("4♡ ",4),("5♡ ",5),("6♡ ",6),("7♡ ",7),("10♡ ",0.5),("11♡ ",0.5),("12♡ ",0.5),
        ("As♢",1),("2♢",2),("3♢",3),("4♢",4),("5♢",5),("6♢",6),("7♢",7),("10♢",0.5),("11♢",0.5),("12♢",0.5),
        ("As♣",1),("2♣",2),("3♣",3),("4♣",4),("5♣",5),("6♣",6),("7♣",7),("10♣",0.5),("11♣",0.5),("12♣",0.5)]

# Creación de una lista vacía.
cartas_barajeadas = []

# barajear
while(not cartas == []): # mientras no esten vacia
    # agregar en las cartas_barajeadas una carta aleatoria del maso de cartas
    cartas_barajeadas.append(cartas.pop(random.randint(0,len(cartas)-1)))
    
# cartas barajeadas    
#?print(cartas_barajeadas)

# crear jugadores con diccionario
j1 = {
    "nombre":"Alfonso",
    "puntos":0,
    "cartas":[]}

j2 = {"nombre":"IA:Polaris",
    "puntos":0,
    "cartas":[]}

# Jugador1 pide cartas
pv = True # es la primera carta
while(True):
    # mostrar nombre
    print("Turno:",j1["nombre"])
    if(pv):
        # la ultima carta del maso de cartas
        carta = cartas_barajeadas.pop()
        # actualiza mano de cartas
        j1["cartas"].append(carta)
        # actualiza puntos
        j1["puntos"]+=carta[1]
        print(j1["cartas"])
        pv = False # ya no es la primera carta
    elif(int(input("Quieres cartas 1, sino 0\n"))):
        carta = cartas_barajeadas.pop()
        j1["cartas"].append(carta)
        j1["puntos"]+=carta[1]
        print(j1["cartas"])
        # detenerse
        input("Enter para continuar ...")
    else:
        pv = True
        break
print(j1["cartas"])

# CPU pide cartas
while(j2["puntos"]<7.5):
    print("Turno",j2["nombre"])
    if(pv):
        carta = cartas_barajeadas.pop()
        j2["cartas"].append(carta)
        j2["puntos"]+=carta[1]
        print(j2["cartas"])
        pv = False
    print("Quieres cartas?")
    time.sleep(2) # espera 2 segundos
    pedir = random.random()>=0.5 # si es mayor a 0.5 si pide carta
    print("Si" if pedir else "No")
    if(pedir):
        carta = cartas_barajeadas.pop()
        j2["cartas"].append(carta)
        j2["puntos"]+=carta[1]
        print(j2["cartas"])
    else:
        break
print(j2["cartas"])

# verifica ganador
j1_status = j1['puntos']<=7.5 # pregunta si puede continuar en juego
j2_status = j2['puntos']<=7.5
# si los dos no se pasaron de 7.5
if(j1_status and j2_status):
    if(j1['puntos']==j2['puntos']):
        print("empate")
    elif(j1['puntos']<j2['puntos']):
        print(f"el ganador es = {j2}")
    else:
        print(f"el ganador es = {j1}")
elif(not j1_status and not j2_status):
    print("Nadie gana")
else: # si al menos uno no se paso de 7.5
    print(f"el ganador es = {j1}" if j1_status else f"el ganador es = {j2}")