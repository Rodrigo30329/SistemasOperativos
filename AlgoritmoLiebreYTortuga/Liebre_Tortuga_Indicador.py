from random import randint
from threading import Thread
import threading
import time

Completo=False
Tortuga = "Tortuga"
Liebre = "Liebre"

AR=3
R=6
AL=1
D=0
GS=9
RG=1
PS=1
RP=2

EventoT = [AR, AR, AR, AR, AR, R, R, AL, AL, AL]
EventoL = [D, D, GS, GS, RG, PS, PS, PS, RP, RP]

class Tortuga(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.NT=0
    def run(self):
        self.NT=randint(0, len(EventoT)-1)
      
class Liebre(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.NL=0
    def run(self):
        self.NL=randint(0, len(EventoL)-1)

def LiebrevsTortuga():
    Completo=False
    x=0
    y=0
    print("La carrera ha comenzado")
    while Completo!=True:
        liebre=Liebre()
        liebre.start()
        ves=liebre.NL
        tortuga=Tortuga()
        tortuga.start()
        ves2=tortuga.NT
        movl=EventoL[ves]
        movt=EventoT[ves2]
        if(x==0):
            if(ves==4 or ves==8 or ves==9):
                movl=1
            else:
                movl=movl
        x=x+movl

        if(y==0):
            if(ves2==5 or ves2==6):
                movt=1
            else:
                movt=movt
        y=y+movt

        time.sleep(1)

        if(x>=200):
            if(y<200):
                print("La liebre ha llegado a 200")
                print("La tortuga ha terminado en " + str(y))
                Completo=True
            if(y>=200):
                print("Ha habido un empate")
                Completo=True
        elif(y>=200):
            if(x<200):
                print("La tortuga ha ganado")
                print("La liebre ha terminado en " + str(x))
                Completo=True
            if(x>=200):
                print("Ha habido un empate")
                Completo=True
        else:
            print("La tortuga va en " + str(y))
            print("La liebre va en " + str(x))
            
def Carrera():  
    carrera = threading.Thread(name='carrera', target=LiebrevsTortuga)    
    carrera.start()

Carrera()

