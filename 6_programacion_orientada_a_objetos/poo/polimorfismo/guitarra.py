from instrumento import Instrumento
class Guitarra(Instrumento):
    def __init__(self,tipo,marca,clasificacion,genero):
        Instrumento.__init__(self,tipo, marca, clasificacion)
        self.genero = genero