#Crea un numero casuale tra 10 e 20, mettilo in una variabile z e stampalo

import random
z=random.randint(10,20)
print(z)

#Riempi una lista (chiamata listone1) con z numeri casuali tra 0 e 20, dove z è la variabile creata al punto 1.
listone1=[]
for i in range(z):
    listone1.append(random.randint(0,20))


#Creare una lista (chiamata listone2) con tutti i numeri della lista listone1 (riempita al punto 2) che sono minori della lunghezza della lista (z)
#Stampa tutti i valori di listone1 che non sono stati messi in listone2
listone2=[]
for valorilista1 in listone1:
    if valorilista1<z:
        listone2.append(valorilista1)
    else:
        print(valorilista1)


#Eleva al quadrato tutti i valori della lista listone2. (es: 5-> 25)
listaquadrato=[]
for valorilista2 in listone2:
    listaquadrato.append(pow(valorilista2, 2))

listone2.clear()
listone2.extend(listaquadrato)

#Fai la somma di tutti i valori di listone2 maggiori di z e stampa il risultato (risultone)
risultone=0
for valorilista2 in listone2:
    if valorilista2>z:
        risultone=risultone+valorilista2
print(risultone)

#Se risultone sommato alla tua età è maggiore della lunghezza di listone2, stampa 'evviva' Altrimenti stampa 'buuuuu'
if risultone+18>len(listone2):
    print("evviva")
else:
    print("buuuuu")
    

