from animal import Animal
from mascota import Mascota
from cocodrilo import Cocodrilo
def main():
    c1 = Cocodrilo("Terrestre","Personas",4,"rrrrr")
    m1 = Mascota("Terrestre","Croquetas",4,"Guau Guau","Yo","Firulais")
    m1.setEdad(2)
    print(m1.getEdad())
    
    if(int(m1.getEdad())>2):
        print("Adulto")
    else:
        print("Cachorro")
    
    # print(m1)
    # print(c1)
if __name__ == "__main__":
    main()