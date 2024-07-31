# Tarea subir a github


Lista = [2,2,3,6,5,0,3]
Lista2 = [3,3,0,2,1,0,1]
def Promedio1(Lista:list):
    m= 0
    for x in Lista:
       m += x
    return f" el promedio es {m/len(Lista)}"
     
print(Promedio1(Lista))

def ProductoPunto(Lista1:list, Lista2:list):
    Suma = 0
    for x in range(0, len(Lista1)):
        Mul = Lista1[x] * Lista2[x]
        Suma += Mul
    return f" el producto punto es {Suma}"

print(ProductoPunto(Lista, Lista2))

def ProductoDirecto(Lista1:list, Lista2:list):
    ListaFinal = []
    for x in range(0, len(Lista1)):
        Mul = Lista1[x] * Lista2[x]
        ListaFinal.append(Mul)
    return f" el producto directo es {ListaFinal}"

print(ProductoDirecto(Lista, Lista2))

def MedianaDeUnaLista(Lista:list):
    Lista.sort()
    if len(Lista) % 2 == 0:
        x = len(Lista)/2
        x = int(x)
        Suma = Lista[x-1] + Lista[x]
        return f" la mediana de la lista es {Suma/2}"
    else:
        x = (len(Lista) - 1)/2
        x = int(x)
        return f" la mediana de la lista es {Lista[x]}"

print(MedianaDeUnaLista(Lista))

def CerosAlFinal(Lista:list):
    for x in range(0, len(Lista)):
        if Lista[x] == 0:
            Lista.append(0)
            Lista.pop(x)
    return f" la lista final es {Lista}"
print(CerosAlFinal(Lista2))