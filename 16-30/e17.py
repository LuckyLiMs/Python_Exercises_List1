# Feito por Flávio Luis

# Crie uma lista de 5 palavras. Use um laço for para criar uma nova lista que 
# contenha as palavras ao contrário. 

palavras = ["Marvel", "Sol", "Estrela", "carro", "balão"]

palavrasInvertidas = []

for palavra in palavras:
  
    inverso = palavra[::-1]
    palavrasInvertidas.append(inverso)

print(palavrasInvertidas)