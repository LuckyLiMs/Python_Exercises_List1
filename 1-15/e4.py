# Feito por flávio Luis

# Crie uma lista com 8 números. Use um laço for para criar uma nova lista que 
# contenha apenas os números pares. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

numerosPares = []

for numero in numbers:
    if numero %2 == 0:

        numerosPares.append(numero)


print(numerosPares)