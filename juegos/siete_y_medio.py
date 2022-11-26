import random 
cartas = [
    ("As oros", 1),
    ("2 oros", 2),
    ("3 oros", 3),
    ("4 oros", 4),
    ("5 oros", 5),
    ("6 oros", 7),
    ("7 oros", 8),
    ("10 oros", 0.5),
    ("11 oros", 0.5),
    ("12 oros", 0.5),   
    ("As copas", 1),
    ("2 copas", 2),
    ("3 copas", 3),
    ("4 copas", 4),
    ("5 copas", 5),
    ("6 copas", 7),
    ("7 copas", 8),
    ("10 copas", 0.5),
    ("11 copas", 0.5),
    ("12 copas", 0.5),   
    ("As espadas", 1),
    ("2 espadas", 2),
    ("3 espadas", 3),
    ("4 espadas", 4),
    ("5 espadas", 5),
    ("6 espadas", 7),
    ("7 espadas", 8),
    ("10 espadas", 0.5),
    ("11 espadas", 0.5),
    ("12 espadas", 0.5),
    ("As bastos", 1),
    ("2 bastos", 2),
    ("3 bastos", 3),
    ("4 bastos", 4),
    ("5 bastos", 5),
    ("6 bastos", 7),
    ("7 bastos", 8),
    ("10 bastos", 0.5),
    ("11 bastos", 0.5),
    ("12 bastos", 0.5),   
]  
# Guardar cartas random
cartas_barajeadas = []
# barajear
while(not cartas == []): #mientras no esten vacia
    cartas_barajeadas.append(cartas.pop(random.randint(0,len(cartas)-1)))
# cartas barajeadas
print(cartas_barajeadas)    

#A jugar/Reglas
# Necesitamos 2 jugadores 
# Jugadores = int(input("Ingresa el número de jugadores"))
J1 = "Persona1"
J2 = "Yen"

# Inicialmente tenemos puntos en cero
puntos_J1 = 0
puntos_J2 = 0

J1 = int(input("¿Quieres una cart "))
manoJ1 = cartas_barajeadas.pop ()
puntosJ1 += manoJ1 [-1][1]



# El ganador deberá tener 7.5 pts
if(J1 = 7.5):
    print("Ganaste")
else:
    print("No ")


Gana_puntos = 7.5 

Pierde > 7.5 

Gana puntos_J1 > puntos_J2