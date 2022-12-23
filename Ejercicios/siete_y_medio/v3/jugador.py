class Jugador:
    def __init__(self,nick):
        self.__nick = nick

# getters y setters
    @property
    def nick(self):
        return self.__nick
    @nick.setter
    def nick(self,nick):
        self.__nick = nick