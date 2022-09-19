import threading

def Contar0a10():
    contador=0
    while contador<10:
        contador+=1
        HActual =  threading.current_thread().getName()
        IdHilo = threading.current_thread().ident
        print('El Hilo '+ HActual + ' identificado con: ', IdHilo, ' va en :', contador)
        if(contador==10):
            print('El Hilo '+ HActual + ' llego a 10 ')

def Contar10a20():
    contador=10
    while contador<20:
        contador+=1
        HActual =  threading.current_thread().getName()
        IdHilo = threading.current_thread().ident
        print('El Hilo '+ HActual + ' identificado con: ', IdHilo, ' va en :', contador)
        if(contador==20):
            print('El Hilo '+ HActual + ' llego a 20 ')

def ContarAlTiempo():
    NHilos = 2    
    for NHilo in range(NHilos):
        hilo = threading.Thread(name='%s' %NHilo , target=Contar0a10)    
        hilo.start()

    for NHilo in range(NHilos):
        hilo = threading.Thread(name='%s' %NHilo , target=Contar10a20)    
        hilo.start()

ContarAlTiempo()