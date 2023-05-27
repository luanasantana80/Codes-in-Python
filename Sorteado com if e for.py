from random import randint
dados=[]
val=0
val2=0
val3=0
val4=0
val5=0
val6=0
for i in range(10):
    dados.append(randint(1,6))
for i in range(10):
    if dados[i]==1:
        val=val+1
    elif dados[i]==2:
        val2=val2+1
    elif dados[i]==3:
        val3=val3+1
    elif dados[i]==4:
        val4=val4+1
    elif dados[i]==5:
        val5=val5+1
    else:
        val6=val6+1
print("valores do dado 10 vezes: 1-",val,"/ 2-",val2,"/ 3-",val3,"/ 4-",val4,"/ 5-",val5,"/ 6-",val6)
