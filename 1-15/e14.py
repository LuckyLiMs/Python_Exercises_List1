# Feito por Flávio Luis

# . Crie uma lista de 10 números. Use um laço while para imprimir cada número 
# até encontrar um que seja maior que 50.


numbers = [25, 34, 10, 23, 44, 31, 29, 1, 3, 56]

i = 0

while i < len(numbers) and numbers[i] <= 50:

    print(numbers[i])
    
    i += 1