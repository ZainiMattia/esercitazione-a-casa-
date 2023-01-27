#Crea un numero casuale tra 10 e 30, mettilo in una variabile n e stampalo
import random
n= random.randrange(10,30)
print(n)


#Riempi una lista list1 con n numeri casuali tra 0 e 30, dove n è la variabile creata al punto 1.
list1=[]
for i in range(n):
    list1.append(random.randrange(0,30))
print(list1)





#Stampa tutti i numeri della lista list1 (riempita al punto 2) che sono maggiori della lunghezza della lista
listavalori= []
for a in list1:
    if a> len (list1): 
        listavalori.append(a)
print(listavalori)


#Riempi una nuova lista list2 con i valori  che non sono stati stampati al punto 3
list2= []
for a in list1:
    if a <= len (list1):
        list2.append(a)
print(list2)


#Rendi negativi tutti i valori della lista list2
for c in range (len(list2)):
    list2[c]=-list2[c]
print(list2)


#Fai la somma di tutti i valori di list2 (dopo averli resi negativi al punto 5) e stampa il risultato (ris)
ris=0
for d in list2:
    ris=ris+d
print(ris)


#Calcola il valore assoluto di ris. Se ris è maggiore della lunghezza di list2 , stampa 'evviva' Altrimenti stampa 'buuuuu'
if abs(ris)> len(list2):
    print("evviva")
else: 
    print("buuuuu")




