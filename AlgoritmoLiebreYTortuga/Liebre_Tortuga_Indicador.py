from random import randint
from threading import Thread
import threading
import time

Completo=False

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

class Tortuga2(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.NT2=0
    def run(self):
        self.NT2=randint(0, len(EventoT)-1)

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
    z=0
    print("La carrera ha comenzado")
    while Completo!=True:
        liebre=Liebre()
        liebre.start()
        ves=liebre.NL
        tortuga=Tortuga()
        tortuga.start()
        ves2=tortuga.NT
        tortuga2=Tortuga2()
        tortuga2.start()
        ves3=tortuga2.NT2
        movl=EventoL[ves]
        movt=EventoT[ves2]
        movt2=EventoT[ves3]
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

        if(z==0):
            if(ves3==5 or ves3==6):
                movt2=1
            else:
                movt2=movt2
        z=z+movt2

        time.sleep(1)

        if(x>=200):
            if(y>=200):
                if(z>=200):
                    print("Hay un triple empate")
                else:
                    print("Ha habido un empate entre la liebre y la tortuga")
                    print("La Tortuga 2 ha terminado en " + str(z))
                Completo=True
            if(z>=200):
                if(y>=200):
                    print("Hay un triple empate")
                else:
                    print("Ha habido un empate entre la liebre y la tortuga 2")
                    print("la liebre ha terminado en " + str(y))
                Completo=True
            if(y<200):
                print("La liebre ha llegado a 200")
                print("La tortuga ha terminado en " + str(y))
                Completo=True
            if(z<200):
                print("La liebre ha llegado a 200")
                print("La tortuga 2 ha terminado en " + str(z))
                Completo=True

        elif(y>=200):
            if(x>=200):
                if(z>=200):
                    print("Hay un triple empate")
                else:
                    print("Ha habido un empate entre la liebre y la tortuga")
                    print("La Tortuga 2 ha terminado en " + str(z))
                Completo=True
            if(z>=200):
                if(x>=200):
                    print("Hay un triple empate")
                else:
                    print("Ha habido un empate entre la tortuga y la tortuga 2")
                    print("la liebre ha terminado en " + str(y))
                Completo=True
            if(x<200):
                print("La tortuga ha llegado a 200")
                print("La liebre ha terminado en " + str(y))
                Completo=True
            if(z<200):
                print("La tortuga ha llegado a 200")
                print("La tortuga 2 ha terminado en " + str(z))
                Completo=True

        elif(z==200):
            if(x>=200):
                if(y>=200):
                    print("Hay un triple empate")
                else:
                    print("Ha habido un empate entre la liebre y la tortuga 2")
                    print("La Tortuga ha terminado en " + str(y))
                Completo=True
            if(y>=200):
                if(x>=200):
                    print("Hay un triple empate")
                else:
                    print("Ha habido un empate entre la tortuga y la tortuga 2")
                    print("la liebre ha terminado en " + str(x))
                Completo=True
            if(x<200):
                print("La tortuga 2 ha llegado a 200")
                print("La liebre ha terminado en " + str(x))
                Completo=True
            if(y<200):
                print("La tortuga 2 ha llegado a 200")
                print("La tortuga ha terminado en " + str(y))
                Completo=True
    
        else:
            print("La liebre va en " + str(x))
            print("La tortuga va en " + str(y))            
            print("La tortuga 2 va en " + str(z))
            
def Carrera():  
    carrera = threading.Thread(name='carrera', target=LiebrevsTortuga)    
    carrera.start()

Carrera()

