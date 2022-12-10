import random,time
import utilidades as utl
#  guardar cartas barajeadas
cartas_barajeadas = utl.barajear()
print(cartas_barajeadas)

# crear jugadores con diccionario
j1 = {
    "nombre":"Alfonso",
    "puntos":0,
    "cartas":[]}

j2 = {"nombre":"IA:Polaris",
    "puntos":0,
    "cartas":[]}

# Jugador1 pide cartas
pv_1 = True

while(True):
    # mostrar nombre
    print("Turno:",j1["nombre"])
    if(pv_1):
        carta = cartas_barajeadas.pop()
        j1["cartas"].append(carta)
        j1["puntos"]+=carta[1]
        print(j1["cartas"])
        pv_1 = False
    if(int(input("Quieres cartas 1, sino 0\n"))):
        carta = cartas_barajeadas.pop()
        j1["cartas"].append(carta)
        j1["puntos"]+=carta[1]
        print(j1["cartas"])
        # detenerse
        input()
    else:
        break
print(j1["cartas"])

# CPU pide cartas
pv_cpu = True
while(j2["puntos"]<7.5):
    print("Turno",j2["nombre"])
    if(pv_cpu):
        carta = cartas_barajeadas.pop()
        j2["cartas"].append(carta)
        j2["puntos"]+=carta[1]
        print(j2["cartas"])
    print("Quieres cartas?")
    time.sleep(2)
    pedir = random.random()>=0.5
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

if(j1_status and j2_status):
    if(j1['puntos']==j2['puntos']):
        print("empate")
    elif(j1['puntos']<j2['puntos']):
        print(f"el ganador es = {j2}")
    else:
        print(f"el ganador es = {j1}")
else:
    print(f"el ganador es = {j1}" if j1 else f"el ganador es = {j2}")