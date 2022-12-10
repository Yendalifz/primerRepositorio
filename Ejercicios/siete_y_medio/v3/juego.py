class Juego:
    def __init__(self,jugadores, reglas):
        self.__jugadores = jugadores
        self.__reglas = reglas
        
    def __menu(self):
        pass
    
    def inicio(self):
        self.__menu()
        pass
    def getReglas(self):
        return self.__reglas
    
    def setReglas(self,reglas):
        self.__reglas = reglas