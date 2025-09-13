# Lucas dos Santos Siqueira
# 43 - Crie um dicionário que conte a frequência de cada letra em uma frase. Exemplo: {'a': 3, 'b': 1, ...}. Use um laço for para percorrer a frase e atualizar o dicionário.

phrase = "Em Monster Hunter, os caçadores enfrentam uma diversidade impressionante de monstros colossais e selvagens em ambientes exuberantes e desafiadores, utilizando uma variedade de armas e estratégias para dominar cada criatura, explorando armadilhas, equipamentos aprimorados e trabalho em equipe para sobreviver e triunfar em batalhas épicas que testam habilidade, paciência e coragem a cada caçada."

letterFrequency={
  "a": 0,
  "b": 0,
  "c": 0,
  "d": 0,
  "e": 0,
  "f": 0,
  "g": 0,
  "h": 0,
  "i": 0,
  "j": 0,
  "k": 0,
  "l": 0,
  "m": 0,
  "n": 0,
  "o": 0,
  "p": 0,
  "q": 0,
  "r": 0,
  "s": 0,
  "t": 0,
  "u": 0,
  "v": 0,
  "w": 0,
  "x": 0,
  "y": 0,
  "z": 0
}

print(f"\nFrase:\n{phrase}\n")
for letter in phrase.lower():
    if letter in letterFrequency:
        letterFrequency[letter] += 1

print(f"Frequência de letras na frase:\n")
for data in letterFrequency:
    print(f"{data} : {letterFrequency[data]}")
# Lucas dos Santos Siqueira