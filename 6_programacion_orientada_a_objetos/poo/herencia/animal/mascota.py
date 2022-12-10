from animal import Animal
class Mascota(Animal):
    
    def __init__(self,especie,alimentacion,numero_de_patas,sonido,duenio,alias):
        Animal.__init__(self,especie,alimentacion,numero_de_patas,sonido)
        self.__alias = alias
        self.__duenio = duenio
        self.__edad = 0
        
    def identificacion(self):
        pass

    def duenio(self):
        return self.__duenio
    
    def cartilla_vacunacion():
        pass
    
    def alias(self):
        return self.__alias
    
    def getEdad(self)->int:
        return self.__edad
    
    def setEdad(self,edad:int):
        """establece una edad

        Args:
            edad (int): validar que si es negativo lo establece en 0
        """
        if edad < 0:
            self.__edad = 0
        else:
            self.__edad = edad
    
    def __str__(self):
        return f'''alias: {self.__alias}
dueño: {self.__duenio}
    '''
    
    