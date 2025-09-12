# Lucas dos Santos Siqueira
# 31 - Crie um dicionário com 3 nomes de cidades e seus respectivos estados. Use um laço for para imprimir cada par de chave e valor.

city={
    "Rezende" : "RJ", 
    "Lorena" : "SP", 
    "Contagem" : "MG",
}

for address in city:
    estate = city[address]
    print(address, ":" , estate)
# Lucas dos Santos Siqueira