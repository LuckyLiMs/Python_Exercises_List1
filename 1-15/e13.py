# Feito por Flavio Luis

# Crie uma lista de 5 strings, onde cada string representa um número. Use um 
# laço for para converter cada string para um número inteiro e armazenar em 
# uma nova lista. 



numerosEmString = ["15", "23", "8", "104", "5"]

numerosInteiro = []

for stringNumero in numerosEmString:
 
    numero = int(stringNumero)
    numerosInteiro.append(numero)

print(f"Nova lista (de inteiros):  {numerosInteiro}")

