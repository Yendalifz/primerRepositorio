class Animal:
    def __init__(self,especie,alimentacion,numero_de_patas,sonido):
        self.__especie = especie
        self.__numero_patas = numero_de_patas
        self.__alimentacion = alimentacion
        self.__clase = None
        self.__sonido = sonido
        
    def __comen(self):
        print(f" soy {self.__especie} y me alimento de {self.__alimentacion}")
    
    def tipoSonido(self):
        print(f"{self.__especie}: {self.__sonido}")
    
    def setClase(self,clase):
        self.__clase = clase
    
    #Sobre escribir para que no imprima la memoria
    def __str__(self):
        return f''' especie: {self.__especie}
numero_patas: {self.__numero_patas}
alimentación: {self.__alimentacion}
clase: {self.__clase}
sonido: {self.__sonido}
    '''   