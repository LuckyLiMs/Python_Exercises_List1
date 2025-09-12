# Lucas dos Santos Siqueira
# 38 -  Crie um dicionário com 5 nomes de cidades e suas populações. Use um laço for para imprimir apenas as cidades com mais de 1 milhão de habitantes.

cities={
    "Campinas" : 1138309,
    "Sorocaba" : 723574,
    "Juiz de Fora" : 568973,
    "São Paulo" : 11451245,
    "Rio de Janeiro" : 6211423,
}

print("\nCidades com mais de um milhão de habitantes: \n")
for data in cities:
    if cities[data] > 1000000:
        print(f"{data} : {cities[data]}")
# Lucas dos Santos Siqueira