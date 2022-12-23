from juego import Juego
import utilidades as utl
import os
from jugadorDeSiete import JugadorDeSiete
class SieteYMedio(Juego):
    
    def __init__(self):
        Juego.__init__(self,"Siete y medio")
        self.__Jugadores = []
        self.__baraja = utl.crear_cartas()

    def inicio(self):
        os.system('cls')
        while(True):
            opt = utl.menu(self.nombre,"Jugador vs jugador","Jugador vs CPU","CPU vs CPU","Salir",error="Elegiste una opción incorrecta intenta de nuevo")
            if(opt!=4):
                os.system('cls')
                if(opt==1):
                    self.__Jugadores.append(utl.crearJugador(True))
                    self.__Jugadores.append(utl.crearJugador(True))
                elif(opt==2):
                    self.__Jugadores.append(utl.crearJugador(True))
                    self.__Jugadores.append(utl.crearJugador(False))
                elif(opt==3):
                    self.__Jugadores.append(utl.crearJugador(False))
                    self.__Jugadores.append(utl.crearJugador(False))
                ganador = self.__inicia_el_juego(self.__Jugadores[0], self.__Jugadores[1])
                os.system("cls")
                try:
                    print(f"El ganador es: {ganador.nick} puntos: {ganador.puntos}")
                    utl.imprimeMano(ganador.mano_de_cartas)
                except:
                    print(ganador["mensaje"])
                input("Enter para continuar...")
                seguir=utl.menu("Continuar","si","no",error="Elegiste una opción incorrecta intenta de nuevo")
                if(seguir==1):
                    self.__reinciar()
                else:
                    break
            else:
                print("salir")
                break
        print("Adios")

    def __inicia_el_juego(self,jugador1:JugadorDeSiete, jugador2:JugadorDeSiete) -> JugadorDeSiete:
        """Los jugadores comienzan a pedir cartas.
        Args:
            jugador1 (JugadorDeSiete)
            jugador2 (JugadorDeSiete)

        Returns:
            JugadorDeSiete: retorna al ganador
        """
        self.__jugar(jugador1)
        
        self.__jugar(jugador2)
        return self.__verificaGanador(jugador1, jugador2)
    
    def __jugar(self,jugador: JugadorDeSiete):
        """Los jugadores pueden pedir cartas.
        Args:
            jugador (JugadorDeSiete)
        """
        primera_carta = True
        jugar = True
        while (jugar):
            os.system('cls')
            if (not primera_carta):
                print(f"Mano de {jugador.nick}")
                utl.imprimeMano(jugador.mano_de_cartas)
                if (self.__regla(jugador) and jugador.seguir_jugando(f"Quieres seguir jugando {jugador.nick}? si:1 no:0  ")):
                    self.__ronda(jugador)
                else:
                    jugar = False
            else:
                self.__ronda(jugador)
                primera_carta = False
        input("Enter para continuar....")
    def __regla(self,jugador:JugadorDeSiete)->bool:
        return True if jugador.calcular_puntos()<=7.5 else False

    def __ronda(self,jugador: JugadorDeSiete):
        """El jugador toma una carta. y acumula puntos.
        Args:
            jugador (JugadorDeSiete): tiene que tomar la decisión ( no cpu).
        """
        jugador.pedir_carta(self.__baraja.pop())
    
    def __verificaGanador(self,jugador1: JugadorDeSiete, jugador2: JugadorDeSiete) -> JugadorDeSiete:
        """Verifica que jugador gano, si empataron o si nadie gano.
        Args:
            jugador1 (dict): tiene que tener la llave puntos.
            jugador2 (dict): '''.
        Returns:
            dict: retorna el jugador ganador, en case de empate un dict("mensaje":mensaje).
        """
        if (self.__regla(jugador1) and self.__regla(jugador2)):
            if (jugador1.puntos == jugador2.puntos):
                return {"mensaje": "Empate"}
            elif (jugador1.puntos < jugador2.puntos):
                return jugador2
            else:
                return jugador1
        elif (not self.__regla(jugador1) and not self.__regla(jugador2)):
            return {"mensaje": "Ninguno gana"}
        else:
            return jugador1 if self.__regla(jugador1) else jugador2

    def __reinciar(self):
        self.__baraja = utl.crear_cartas()
        self.__Jugadores = []

# getters y setters
    @property
    def Jugadores(self):
        return self.__Jugadores
    @Jugadores.setter
    def Jugadores(self,Jugadores):
        self.__Jugadores = Jugadores

    @property
    def baraja(self):
        return self.__baraja
    @baraja.setter
    def baraja(self,baraja):
        self.__baraja = baraja