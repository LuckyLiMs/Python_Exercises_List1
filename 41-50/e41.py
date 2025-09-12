# Lucas dos Santos Siqueira
# 41 - Crie um dicionário com 5 nomes de pessoas e suas idades. Use um laço for para criar  uma nova  lista  contendo  apenas  os  nomes  das  pessoas  com  mais  de  30 anos. 

peoples={
    "Lucas" : 19,
    "Yoda" : 900,
    "Dalton" : 19,
    "Eduarda" : 18,
    "Paulo" : 79,
}

only_30Plus = []
print("\nDicionário de todas pessoas:\n")
for data in peoples:
    print(f"{data} : {peoples[data]}")
    if peoples[data] > 30:
        only_30Plus.append(data)

print("\nLista de todas pessoas com mais de 30 anos:\n")
for oldOnes in only_30Plus:
    print(f"{oldOnes}")
# Lucas dos Santos Siqueira