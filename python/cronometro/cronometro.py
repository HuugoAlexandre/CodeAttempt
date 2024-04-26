import os
import time

"""
Cronômetro simples. Possivelmente por conta do tempo de processamento, perde-se 
2 segundos por minuto, que faz a diferença por se tratar de um cronômetro.
Pra corrigir isso, poderia definir +2sec a cada passagem de minuto ou
diminuir o sleep.
"""

class Cronometro:
    def __init__(self, segundos = 0, minutos = 0, horas = 0) -> None:
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __repr__(self) -> str:
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'
        
    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.resto = self.segundos - 60
            self.segundos = self.resto + 2
            self.minutos += 1
            if self.minutos >= 60:
                self.resto = self.minutos - 60
                self.minutos = self.resto
                self.horas += 1
                if self.horas > 99:
                    print("Fora do limite.")
                    print("Saindo em 5 segundos...")
                    time.sleep(5)
                    exit()

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)

# cronometro = Cronometro(50, 59)   
# cronometro = Cronometro(55, 59, 99)
# cronometro = Cronometro(50, 43, 2)      
cronometro = Cronometro()
cronometro.start()         