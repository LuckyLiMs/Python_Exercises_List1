# Feito por Flávio Luis

#  Crie uma lista com 5 nomes. Use um laço for para imprimir os nomes em ordem 
# alfabética inversa. 


nomes = ["Flávio", "Ana", "Lucas", "George", "Maria"]

print("Ordem alfabética inversa")

for nome in sorted(nomes, reverse=True):
    print(nome)