# Feito por Flávio Luis 

# . Crie uma lista com 10 nomes de pessoas. Use um laço while para imprimir os 
# nomes um por um, parando quando encontrar o nome "Ana".


nomes = ["Flávio", "joão", "clarissa", "Gabriela", "Julia", "Maria", "Ronaldo", "josé", "Ana", "Cleyton"]


i = 0

while i < len(nomes) and nomes[i] != "Ana":

    print(nomes[i])
    
    i += 1