# Feito por Flávio Luis 

# Crie uma lista de 10 números inteiros. Use um laço for para calcular e imprimir 
# a soma de todos os números da lista. 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for numero in numbers:
    soma = soma + numero

    print(f"A soma de todos os números é: {soma}" )