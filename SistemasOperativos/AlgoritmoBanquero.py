
import numpy as np

RecursosTotales = []
ProcesosTotales = []
RecursosMaximos = []
RecursosDisponibles = []
RTemp = []
EstadoProceso = []
cont = 0

NRecursos = int(input("ingrese el numero de recursos a usar : "))
for i in range(NRecursos+1):
    RecursosTotales.append("R"+str(i))
RecursosTotales.remove("R0")

NProcesos = int(input("ingrese el numero de procesos a usar : "))
for i in range(NProcesos+1):
    ProcesosTotales.append("P"+str(i))
ProcesosTotales.remove("P0")

for i in range(NRecursos):
    RMax = int(input("ingrese la cantidad disponible de recurso "+RecursosTotales[i]+" : "))
    RecursosMaximos.append(RMax)
    RecursosDisponibles.append(RMax)
    RTemp.append(RMax)

RecursosNecesarios=np.empty([NProcesos, NRecursos])
for i in range(NProcesos):
    for j in range(NRecursos):
        val=int(input("ingrese la cantidad de recurso "+RecursosTotales[j]+" que usa el proceso "+ProcesosTotales[i]+" : "))
        RecursosNecesarios[i,j] = val

RecursosActual=np.empty([NProcesos, NRecursos])
for i in range(NProcesos):
    for j in range(NRecursos):
        RecursosActual[i,j] = 0

RecursosNecesariosActual=np.empty([NProcesos, NRecursos])
for i in range(NProcesos):
    for j in range(NRecursos):
        RecursosNecesariosActual[i,j] = RecursosNecesarios[i,j] - RecursosActual[i,j]

for i in range(NProcesos):
    EstadoProceso.append("NO")
contpro=0
while contpro<NProcesos:
    for i in range(NProcesos):
        for j in range(NRecursos):
            if RecursosNecesariosActual[i,j] <= RecursosDisponibles[j]:
                cont=cont+1
                RTemp[j]=RTemp[j]-RecursosNecesariosActual[i,j]
            if cont==NRecursos: 
                print("El proceso "+ProcesosTotales[i]+" puede ejecturase")
                EstadoProceso[i]="SI"
                for x in range(NRecursos):
                    RecursosDisponibles[x]=RTemp[x]
                cont=0
            elif(cont==j):
                for x in range(NRecursos):
                    RTemp[x]=RecursosDisponibles[x]
        RTemp[j] = RecursosDisponibles[j]
        if i==0 and EstadoProceso[i]=="SI":
            print("El proceso "+ProcesosTotales[i]+" fue ejectutado")
            RTemp[i]=RecursosDisponibles[i]
            contpro=contpro+1
        if i!=0 and EstadoProceso[i-1]=="SI":
            print("El proceso "+ProcesosTotales[i]+" fue ejectutado")
            RTemp[i]=RecursosDisponibles[i]
            contpro=contpro+1

print(RTemp)
print(RecursosMaximos)
print(RecursosNecesarios)
print(RecursosActual)
print(RecursosNecesariosActual)
print(RecursosTotales)
print(ProcesosTotales)
print(EstadoProceso)
