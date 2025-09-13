# Feito por Flávio Luis

#  Crie uma lista de 5 nomes de pessoas. Use um laço for para criar uma nova lista 
# que contenha apenas os nomes com mais de 5 letras.


nomes = ["Alice", "Marcos", "Roberto", "Michael", "Diego"]


nomesMaiores = []

for letras in nomes:
    if len(letras) > 5:
        nomesMaiores.append(letras)


print(nomesMaiores)
        