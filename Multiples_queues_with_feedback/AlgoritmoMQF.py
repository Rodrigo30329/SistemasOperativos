import collections
from typing import OrderedDict

# def IngresarDatos():
#     Nprocesos = int(input('Ingrese el numero de procesos'))
#     Llegada = int(input('Ingrese las posiciones de llegada'))
#     PrioridadesIniciales = int(input('Ingrese las prioridades iniciales'))
#     ColaActual = int(input('Ingrese la cola actual'))
#     TiempoMaximo = int(input('Ingrese el tiempo maximo de un proceso en cola'))
#     return Nprocesos, Llegada, PrioridadesIniciales, ColaActual,TiempoMaximo

Procesos = ['P1', 'P2', 'P3', 'P4']
Llegada = [3, 2, 1, 4]
PrioridadesIni = [300, 300, 200, 100]
Recursos = [200, 100, 150, 100]
Maximo = 10
Completos = [False, False, False, False]
Ncolas = 1
Cola = ['C1']

def OrdenarLlegada(Procesos, Prioridades):
    for i in range(len(PrioridadesIni)):
        PrioridadesIni[i] = PrioridadesIni[i] - Llegada[i]
    DictPP = {Prioridades[i]: Procesos[i] for i in range(len(Prioridades))}
    Orden = collections.OrderedDict(sorted(DictPP.items()))
    Orden = OrderedDict(reversed(list(Orden.items())))
    return Orden

def OrdenarRecursos(Procesos, Recursos):
    DictRP = {Procesos[i]: Recursos[i] for i in range(len(Procesos))}
    OrdenR = collections.OrderedDict(sorted(DictRP.items()))
    return OrdenR

def EjecutarProceso(Orden, OrdenR, Maximo):
    Prioridades = list(Orden.keys())
    Procesos = list(Orden.values())
    ProcesosAsignado = list(OrdenR.keys())
    Recursos = list(OrdenR.values())
    print(Prioridades, Procesos, Recursos, ProcesosAsignado)
    c=0
    Proceso = Procesos[0]
    pos = ProcesosAsignado.index(Proceso)
    Completado = False
    while c < Maximo:
        Recursos[pos] = Recursos[pos]-10 
        if Recursos[pos] == 0:
            Recursos[pos] = 0 
        c=c+1
    if(Recursos[pos]!=0):
        Prioridades[0] = Prioridades[0]-100
    elif(Recursos[pos]==0):
        Prioridades[pos] = 0
        Completado = 1
        print('Proceso '+Procesos[0]+' terminado')
    Orden = OrdenarLlegada(Procesos, Prioridades)
    return Completado, Orden

def VerificarCompletado(Completados, Completado, Orden, Ncolas):
    Ncol = Ncolas
    for i in range(Completado):
        if Completados[i] != Completado:
            Completados[i] = True
            Orden.popitem()
    if Completado == False:
        Ncol=Ncol+1
    return Completados, Orden, Ncol

# def Colas(Completados, Orden, Ncolas, Colas, Recursos, Maximo):
#     if Completados[0] == False:
#         Cola.append("C"+str(Ncolas))
#         EjecutarProceso(Orden, Recursos, Maximo)
 
Completado, Orden=EjecutarProceso(OrdenarLlegada(Procesos, PrioridadesIni), OrdenarRecursos(Procesos, Recursos) , Maximo)
Completados, Orden, Ncolas = VerificarCompletado(Completos, Completado, Orden, Ncolas)
# Colas(Completados, Orden, Ncolas, Colas, Recursos, Maximo)

print(Completados, Orden, Ncolas)
