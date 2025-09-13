# Feito por Flávio Luis

#  Crie uma lista de 10 números. Use um laço for para criar uma nova lista com o 
# dobro de cada número. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dobro = []

for numero in numbers:
    if numero == numero:
        dobro.append(numero*2)


print(dobro)