# Feito por Flávio Luis

# Crie uma lista de 10 números. Use um laço for para encontrar e imprimir o 
# maior número da lista. 


numbers = [1, 2, 3, 4, 23, 8, 9, 10, 11, 6]

maiorNumero = numbers[0]

for numero in numbers:
    if numero > maiorNumero:

        maiorNumero = numero


print(f"O maior número da lista é o: {maiorNumero}")