# Lucas dos Santos Siqueira
# 30 - Crie uma lista de strings. Use um laço for para contar a quantidade de strings que começam com a letra 'P'.
# DISCLAIMER: eu vi que poderia utilizar a função do python startswith() porém quis fazer na mão para aprender de verdade como é feito.

strings = ["Monster Hunter", "Rathalos", "Nargacuga", "Chatacabra", "Paolomu", "Popo", "Pelagus", "Fanged Beasts", "Doshaguma", "Rathian", "Zinogre", "Kirin", "Teostra", "Nergigante", "Kushala Daora", "Congalala", "Rajang", "Seikret", "Palico", "Lirinx", "Linian", "Human", "Troverian", "Wyverian", "Wather People", "Pukei Pukei", "Plesioth", "Primordial Malzeno", "Pink Gypceros"]

def stringsWithP(strings):
    have_P = 0
    for words in strings:
        if len(words) > 0: # verifica se a palavra está vazia
            first_letter = words[0].lower() # lembrando que uma palavra pode ser resumidamente dita como uma lista de letras, então se atribui a primeira letra a variável first_letter aqui
            if first_letter == "p":
                have_P += 1
    return have_P
print(f"Lista de Strings: \n{strings}\nQuantidade de palavras que começam com a letra P: \n{stringsWithP(strings)}")
# Lucas dos Santos Siqueira