# Feito por Flávio Luis 

#  Crie uma lista de 5 palavras. Use um laço for para criar uma nova lista contendo 
# as palavras em maiúsculas.


palavras = ["gato", "cachorro", "carro", "macarrão", "starwars"]

palavrasMaiusculas = []

for palavra in palavras:
  
  palavrasMaiusculas.append(palavra.upper())


print("Lista em maiúsculas:", palavrasMaiusculas)