#Se crea la estructura principal del programa, y la lógica de programación del juego. Importando los archivos.
import random
import Palabras
Palabras.lista_palabras
from dibujo import AHORCADO

def juego_ahorcado(elegir_palabra): #Palabra seleccionada al azar
    fin_del_juego = False  #El juego debe seguir o no.

    vidas = len(AHORCADO) - 1  #Número de vidas 6.

    letras_encontradas = []   #Guardamos las letras encontradas correctamente.
    for _ in range(len(letras_encontradas)):
        letras_encontradas += "_"  #Se rellenan los guiones con las letras encontradas.
    while not fin_del_juego: #Iniciamos el ciclo
        encontrar = input("Encontrar una letra: ").lower()
    if encontrar in letras_encontradas:
        print(f"Ya adivinaste {encontrar}")  #No se quita vida por las letras anteriormente mencionadas 
    
    for posicion in range(len(elegir_palabra)): #Se usa el ciclo para ver si ya se encontró la letra correcta y se agrega
        letra = elegir_palabra[posicion]
        if letra == encontrar:
            letras_encontradas[posicion] = letra
    print(f"{' '.join(letras_encontradas)}")
    
    if encontrar not in letras_encontradas: #Si la letra no es la indicada, se reduce una vida.
            print(f"Elegiste {encontrar}, pero no es la palabra, asi que perdiste una vida.")
            vidas -= 1
            if vidas == 0: #Verificamos si las vidas son iguales a cero, de ser asi pierde.
                fin_del_juego = True
                print("Perdiste :(.")
                print(f"La palabra era {elegir_palabra}.") #Mencionamos la palabra correcta.
    if not "_" in letras_encontradas: #SI adivina correctamente, la condición es que ganó el juego.
        fin_del_juego = True
        print("Felicidades. ¡Has ganado!")

    print(AHORCADO[vidas]) #Se imprime el dibujo del muñeco, cada que mencionas letras incorrecta.

if __name__ == " __main__":
    elegir_palabra = random.choice(lista_palabras)
    print(f"Es un {len(elegir_palabra)}-letras palabra.")
    juego_ahorcado(elegir_palabra)
