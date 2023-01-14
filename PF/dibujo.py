'''
dibujar vidas
'''
AHORCADO = ['''
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========''']

def vidas(vidas:int)->str:   #AL AGRGEAR LAS VIDAS AQUI YA NO SE MENCIPNAN EN EL CODIGO DE main.py
      """Retorna el dibujo del ahorcado segun el número de vidas

      Args:
          vidas (int): número de vidas

      Returns:
          str: '''
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                ========='''
      """
      return AHORCADO[len(AHORCADO)-vidas-1]