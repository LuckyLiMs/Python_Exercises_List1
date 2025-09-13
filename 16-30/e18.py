# Feito por Flávio Luis

# Dada uma lista com 15 números, use um laço for para remover todas as 
# duplicatas. Ao final, imprima a lista com apenas valores únicos. 


numeros = [10, 25, 8, 42, 10, 15, 25, 8, 33, 5, 42, 10, 99, 5, 15]

numerosUnicos = []

for numero in numeros:

    if numero not in numerosUnicos:
 
        numerosUnicos.append(numero)


print(numerosUnicos)