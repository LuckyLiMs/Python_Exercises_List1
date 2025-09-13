# Feito por Flávio Luis 

# Crie uma lista com 10 números inteiros. Use um laço for para separar os 
# números pares e ímpares em duas novas listas 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



numerosPares = []

numerosImpar = []

for numero in numbers:
    if numero %2 == 0:

        numerosPares.append(numero)
    else:
        numerosImpar.append(numero)


print(f"Números pares: {numerosPares} ")
print(f"Números impar: {numerosImpar}")