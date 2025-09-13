# Feito por Flávio Luis

#  Crie uma lista com 10 números inteiros. Use um laço for para somar apenas os 
# números negativos. 


numbers = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]

soma  = 0

for numero in numbers:
    if numero < 0:
           soma = soma + numero

  

print(f"A soma de todos os números negativos é: {soma}" )