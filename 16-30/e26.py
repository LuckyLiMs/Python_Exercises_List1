# Lucas dos Santos Siqueira
# Estou fazendo todos os meus códigos em inglês para começar a treinar já a segunda linguagem diretamente na profissão

# 26 - Crie uma lista de strings. Use um laço for para remover todas as strings que contêm a letra 'a'.

# starWars = ["Star Wars", "New Hope", "Empire Strickes Back", "Return of the Jedi", "Phantom Menace", "Clone Wars", "Revenge of the Sith"]

# def removeA(strings):
#     listWithoutA = []
#     # Analisa as Strings
#     for string in strings:
#         have_A = False
#         # Analisa cada letra na String
#         for letter in string:
#             # Verifica se a String possui a letra A
#             if letter == "a":
#                 have_A = True
#                 break
#         # Se não tiver, adiciona na lista que não tem A
#         if have_A == False:
#             listWithoutA.append(string)
#     return listWithoutA

# print(f"Lista com os nomes completos: \n{starWars}\nLista com os nomes sem a letra 'A'\n{removeA(starWars)}")

# Até aí foi bonito e tudo mais porém o enunciado pede para REMOVER as strings que contém a letra 'a', então não posso fazer isso porque estou criando uma lista nova alí na linha 7. Então retrabalhei o código para atender ao enunciado.

# assim a lógica será a seguinte, percorrer as strings como já foi feito, identificar as strings com A, também irei utilizar outra lista, porém agora essa lista será para as strings com A e depois utilizarei a função .remove() do próprio python para remover os valores com A da lista original.

starWars = ["Star Wars", "New Hope", "Empire Strickes Back", "Return of the Jedi", "Phantom Menace", "Clone Wars", "Revenge of the Sith"]

def removeA(strings):
    listWithA = []
    # Analisa as Strings
    for string in strings:
        have_A = False
        # Analisa cada letra na String
        for letter in string:
            # Verifica se a String possui a letra A utilizando a função .lower() do python que passa todos os caracteres para caixa baixa
            if letter.lower() == "a":
                # Se tiver, adiciona na lista que tem A
                have_A = True
                listWithA.append(string)
                break
                # Se não tiver, sai do laço if atual e refaz os anteriores até encontrar
    # Analisa as strings que possuem a letra A, e remove elas da lista principal
    for stringsWithA in listWithA:
        strings.remove(stringsWithA)
    return strings

print(f"Lista com os nomes completos: \n{starWars}\nLista com os nomes sem a letra 'A'\n{removeA(starWars)}")

# Lucas dos Santos Siqueira
