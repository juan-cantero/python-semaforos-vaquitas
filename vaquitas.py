import os
import random
import time
import threading
from puente import Puente

inicioPuente = 10
largoPuente = 20


class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(self.posicion != inicioPuente):
      self.avanzar()
    vaquitaEspera.acquire()
    while(self.posicion != inicioPuente + largoPuente):
      self.avanzar()
    vaquitaEspera.release()

vacas = []
cuantasVacasPasan = input("ingrese cuantas vacas pasan")
vaquitaEspera = threading.Semaphore(int(cuantasVacasPasan))

for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

puente = Puente(10,10)



while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  puente.dibujar()
  for v in vacas:
    v.dibujar()
    
  puente.dibujar()
  time.sleep(0.2)
