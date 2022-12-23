class Carta:
    def __init__(self,figura:str,valor:float):
        self.__figura = figura
        self.__valor = valor
    
    @property
    def figura(self)->str:
        return self.__figura

    @property
    def valor(self)->float:
        return self.__valor
    
    def __str__(self):
        return f"{self.__figura}|{self.__valor}"
