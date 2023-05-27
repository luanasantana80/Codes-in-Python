
coluna=[]
for i in range(5):
    agenda=[]
    for i in range(1):
        agenda.append(str(input("Nome: ")))
        agenda.append(int(input("Telefone: ")))
    coluna.append(agenda)
print(coluna)

busca=str(input("nome da busca: "))
guarda=0
for i in range(5):
    for j in range(1):
        if coluna[j] == busca:
            guarda=coluna[1]
        
print("telefone: ", guarda)
