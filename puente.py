class Puente:
    def __init__(self, inicio, largo):
        self.inicio = inicio
        self.largo = largo
    
    def dibujar(self):
        print(' ' * self.inicio + '=' * self.largo)