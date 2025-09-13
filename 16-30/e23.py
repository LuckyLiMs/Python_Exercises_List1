# Feito por Flávio Luis 

#  Crie duas listas de 5 números cada. Use laços for aninhados para multiplicar 
# cada número da primeira lista por cada número da segunda lista. 




lista1 = [2, 3, 4, 5, 6]
lista2 = [10, 20, 30, 40, 50]


for i in range(len(lista1)):
  
  num1 = lista1[i]
  num2 = lista2[i]
  
  resultado = num1 * num2
  print(f"{num1} x {num2} = {resultado}")
