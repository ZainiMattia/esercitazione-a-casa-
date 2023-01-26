#Crea un numero casuale tra 10 e 30, mettilo in una variabile n e stampalo
import random
n= random.randrange(10,30)
print(n)


#Riempi una lista list1 con n numeri casuali tra 0 e 30, dove n è la variabile creata al punto 1.
list1=[]
for i in range(n):
    list1.append(random.randrange(0,30))
print(list1)
