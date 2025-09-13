# Feito por Flávio Luis

# , Crie uma lista de 10 números. Use um laço for para calcular a média dos 
# números pares

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

somaDosPares = 0  
contadorDePares = 0  

for numero in numbers:
  
  if numero % 2 == 0:
    somaDosPares = somaDosPares + numero  
    contadorDePares = contadorDePares + 1 


if contadorDePares > 0:
    media = somaDosPares / contadorDePares
    print(f"A média dos números pares é: {media}")
