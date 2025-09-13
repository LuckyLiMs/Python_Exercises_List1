# Lucas dos Santos Siqueira
# 50 - Crie um dicionário que mapeie nomes de pessoas para suas listas de hobbies. Use  um  laço  for  para  encontrar  e  imprimir  o  nome  das  pessoas  que  têm "leitura" como um de seus hobbies.

# Resolvi fazer essa em Português Brasileiro para ficar mais legível

pessoas={
  "Lucas" : ["Modelagem 3D", "Desenhar", "Jogar"],
  "Eduarda" : ["Tocar Violão", "Andar de Patins", "Ler"],
  "Dalton" : ["Colecionar", "Jogar", "Codificar"],
  "Bruna" : ["Desenhar", "Ler", "Escrever"],
  "Paulo" : ["Ler", "Jogar", "Calcular"],
}

print(f"\nPessoas que possuem leitura como hobbies\n")
for pessoa in pessoas:
  if "Ler" in pessoas[pessoa]:
    print(f"Nome: {pessoa}")
# Lucas dos Santos Siqueira