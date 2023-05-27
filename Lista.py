altura=[]
peso=[]
nome=[]
for i in range(5):
    altura.append(float(input("altura: ")))
    peso.append(int(input("peso: ")))
    nome.append(str(input("nome: ")))
calculo=[]
for i in range(5):
    calculo.append(peso[i]/(altura[i]*altura[i]))

for i in range(5):
    print(nome[i]," com imc de ",calculo[i]) 
