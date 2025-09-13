# Feito por FLávio Luis

# . Crie uma lista de 5 palavras. Use um laço for para contar e imprimir o número 
# total de vogais em todas as palavras. 


palavras = ["python", "logica", "programacao", "desafio",]

vogais = "aeiou"

totalDeVogais = 0

for palavra in palavras:
   
    for letra in palavra:
        if letra in vogais:
            totalDeVogais += 1 


print(f"O total de vogais em todas as palavras é: {totalDeVogais}")