#Riempi 3 variabili con numeri casuali. Stampa i valori in ordine (dal più piccolo al più grande)
import random
a= random.randrange(0,10)
b= random.randrange(0,10)
c= random.randrange(0,10)
lista=[a, b, c]
lista.sort()
print(lista)


#Riempi una lista con 5 nomi di automobili e una con 4 Moto, unisci le liste. Stampa la lista risultato in ordine alfabetico
listaAuto=["A","B","Z","V"]
listMoto= ["M","C","D","P"]
Listone=listaAuto + listMoto
Listone.sort()
print(Listone)


#Riempi una lista di 50 numeri casuali. Elimina dalla lista tutti i numeri pari. Stampa la lista
Lista1=[]
for i in range(50):
    Lista1.append(random.randrange(0,20))

listaD=[]
for x in Lista1:
    if (x%2)!=0:
        listaD.append(x)
print(listaD)