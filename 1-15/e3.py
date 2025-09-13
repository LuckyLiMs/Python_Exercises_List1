# Feito por Flávio Luis


#  Crie uma lista de 6 notas (valores de 0 a 10). Use um laço for para contar 
# quantas notas são maiores ou iguais a 7 e imprimir o total. 


notas = [1, 4, 9, 8, 2, 10 ]

contador = 0

for nota in notas :
    if nota >= 7:
      
      contador = contador + 1


print(f"O total de notas maiores e iguais a 7 foram: {contador}")    
  