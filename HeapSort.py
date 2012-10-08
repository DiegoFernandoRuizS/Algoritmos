import time

def heapsort(lista,tam):
    tiempo = time.time()
    for k in range(tam-1,-1,-1):
        for i in range(0,k):
            item=lista[i]
            j=(i+1)/2
            while j>=0 and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=j/2
            lista[i]=item;
         temp=lista[0];
    lista[0]=lista[k];
    lista[k]=temp;

def imprimeLista(lista,tam):
    for i in range(0,tam):
        print lista[i]
        print time.time()-tiempo
def leeLista():
    lista=[]
    cn=int(raw_input("Cantidad de numeros a ingresar: "))

    for i in range(0,cn):
        lista.append(int(raw_input("Ingrese numero %d : " % i)))
    return lista

A=leeLista()
heapsort(A,len(A))
imprimeLista(A,len(A))
