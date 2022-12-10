from instrumento import Instrumento
from guitarra import Guitarra
from bateria import Bateria
from bajo import Bajo
from teclado import Teclado
def main():
    g1 = Guitarra("Guitarra","Ibanez","Cuerdas","Blues")
    print(g1.clasificacion)
    bt1 = Bateria("tipo", "marca", "clasificacion")
    b1 = Bajo("tipo", "marca", "clasificacion")
    t1 = Teclado("tipo", "marca", "clasificacion")
    inst:Instrumento = [g1,bt1,b1,t1]
    print(type(g1) == type(bt1))
    
if __name__ == "__main__":
    main()