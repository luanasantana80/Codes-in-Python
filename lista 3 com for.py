from random import randint
lista=[]
lista2=[]
comum=[]
incomum=[]
incomum2=[]
for i in range(11):
   lista.append(randint(10,20))
   lista2.append(randint(10,20))
for i in range(11):
    for j in range(11):
        if lista[i]==lista2[j]:
            comum.append(lista[i])

for i in range(11):
    for j in comum:
        if lista[i]==comum[j]:
            incomum.append(lista[i])
        if lista2[i]==comum[j]:
            incomum2.append(lista2[i])
            
print(comum)
