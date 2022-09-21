
# En un Almacen hay 2 cajeros en que se pregunta si hay más de 5 personas. Se generan aleatoriamente y si hay 5 o más se abre una nueva caja.

import threading
import time
from random import randrange
from threading import Thread

def LlegadaCaja():
    N=randrange(100)
    while N>0:
        contador = 1
        Clientes = list()
        Maximo = 6
        while contador<Maximo:
            N=N-1
            Clientes.append('C'+str(contador))
            print('La caja '+ str(contador) + ' tiene ' + str(contador) + ' clientes ')
            if(contador==5):
                print('La caja '+ str(contador) + ' llego a 5 clientes ')
            contador+=1
            cajero = Cajero()
            cajero.start()
            cp=cajero.comp
            print(Clientes)
            if (cp==True):
                contador=contador-1
                Clientes.pop(-1)
                print(Clientes)
                print('↨')

class Cajero(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.comp = False
    def run(self):
        T=randrange(5)
        time.sleep(T)
        self.comp = True
    
def Distribuir():  
    caja = threading.Thread(name='caja', target=LlegadaCaja)    
    caja.start()

Distribuir()