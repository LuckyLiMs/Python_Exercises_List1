# Lucas dos Santos Siqueira
# 28 - Crie uma lista de 10 números. Use um laço  for para imprimir os números em ordem decrescente.

# numbers = [0,1,2,3,4,5,6,7,8,9]
numbers = [4,1,7,0,9,2,6,3,5,8]
listaDesordenada = numbers.copy()
# a lista original será modificada pela função, então criei uma cópia para guardar seus valores originais

def calcOrdemDecre(numbers):
    # Ordena a lista com for. A ideia aqui é percorrer a lista com for e ver quais são os menores números, sempre fazendo uma identificação binária, se o número da esquerda for menor que o da direita ele é passado para o lado direito e por aí vai até chegar no fim da lista.

    aux = 0 #variável auxiliar para a transferência de um valor para a direita
    for j in range(len(numbers) - 1): # vai passar fazendo a repetição da comparação    
        for i in range(len(numbers) - 1): # vai passar comparando os números, sendo uma comparação binária
            if numbers[i] < numbers[i+1]: # compara o número da esquerda com o da direita, se for menor:
                aux = numbers[i+1] # atribui o valor do da direita à variável auxiliar
                numbers[i+1] = numbers[i] # atribui o valor do da esquerda à direita
                numbers[i] = aux # atribui o valor da variável auxiliar à esquerda

    return numbers

print(f"Lista com os números desordenados: \n{listaDesordenada}\nLista com os números em ordem decrescente: \n{calcOrdemDecre(numbers)}")
# Lucas dos Santos Siqueira