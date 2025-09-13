# Lucas dos Santos Siqueira
# 29 - Crie uma lista de listas (uma matriz 2x3). Use laços for aninhados para imprimir cada elemento. 

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

def impressMatrix(matrix):
    for lines in matrix:
        # for numbers in lines:
        for i in range(len(lines)):
            if i == len(lines) - 1:
                print(f"{lines[i]}")
            else:
                print(f"{lines[i]}, ", end='') # end='' faz o print perder a propriedade automática de quebra de linha no python

print("Matriz:")
impressMatrix(matrix)
# Lucas dos Santos Siqueira