# Lucas dos Santos Siqueira
# 27 - Crie  uma  lista  de  10  números.  Use  um  laço  for  para  encontrar  a  mediana  da lista (após ordená-la)

# numbers = [0,1,2,3,4,5,6,7,8,9]
numbers = [4,1,7,0,9,2,6,3,5,8]
listaDesordenada = numbers.copy()
# a lista original será modificada pela função, então criei uma cópia para guardar seus valores originais

def calcMediana(numbers):
    # Ordena a lista com for. A ideia aqui é percorrer a lista com for e ver quais são os maiores números, sempre fazendo uma identificação binária, se o número da esquerda for maior que o da direita ele é passado para o lado direito e por aí vai até chegar no fim da lista.

    aux = 0 #variável auxiliar para a transferência de um valor para a direita
    for j in range(len(numbers) - 1): # vai passar fazendo a repetição da comparação    
        for i in range(len(numbers) - 1): # vai passar comparando os números, sendo uma comparação binária
            if numbers[i] > numbers[i+1]: # compara o número da esquerda com o da direita, se for:
                aux = numbers[i+1] # atribui o valor do da direita à variável auxiliar
                numbers[i+1] = numbers[i] # atribui o valor do da esquerda à direita
                numbers[i] = aux # atribui o valor da variável auxiliar à esquerda

    # percorrer o meio e fazer a mediana. A mediana de uma lista de quantidade par, é a média dos dois elementos no meio
    mediana = (numbers[4]+numbers[5])/2
    # retornar
    return numbers, mediana

#pega os valores da função e atribui à variáveis
listaOrdenada, mediana = calcMediana(numbers)

print(f"Lista com os números desordenados: \n{listaDesordenada}\nLista com os números ordenados: \n{listaOrdenada}\nMediana da lista: \n{mediana}")
# Lucas dos Santos Siqueira