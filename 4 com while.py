numer=[]
num=0
alfa=0
beta=0
omega=0
alfaMaior=0
resto=0
k=0
while (num>=0):
    numero=0
    numero=int(input("Informe um NUMERO: "))
    num=numero
    if numero>=0:
        numer.append(numero)
        k=k+1
  
print(numer)    
for i in range(k):
    if numer[i]>=0 and numer[i]<=25:
        alfa=alfa+1
    elif numer[i]>=26 and numer[i]<=50:
        beta=beta+1
    elif numer[i]>=51 and numer[i]<=75:
        omega=omega+1
    elif numer[i]>=76 and numer[i]<=99:
        alfaMaior=alfaMaior+1
    else:
        resto=resto+1
print("0-25: ",alfa)
print("26-50: ",beta)
print("51-75: ",omega)
print("76-99: ",alfaMaior)
print("100+: ",resto)
