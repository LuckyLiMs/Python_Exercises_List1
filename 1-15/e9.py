# Feito por Flávio Luis 


# Crie uma lista de 10 números. Use um laço for para encontrar e imprimir o 
# menor número da lista. 


numbers = [ 6, 2, 3, 4, 23, 8, 9, 10, 11, 1]

menorNumero = numbers[0]

for numero in numbers:
    if numero < menorNumero:

        menorNumero = numero


print(f"O menor número da lista é o: {menorNumero}")