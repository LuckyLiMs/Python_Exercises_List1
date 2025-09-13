# Feito por FLávio Luis


#  Crie uma lista de 10 números. Use um laço for para contar quantas vezes o 
# número 5 aparece na lista. 

numbers = [1, 3, 4, 5, 6, 5, 8, 5, 7, 5]


contador = 0

for numero in numbers:
    if numero == 5:
       contador += 1


print(f"O número 5 foi detectado {contador} vezes")