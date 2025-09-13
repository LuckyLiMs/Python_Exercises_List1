# Lucas dos Santos Siqueira
# 48 - Crie  um  dicionário  para  um  produto  com  as  chaves:  nome,  preço, disponível. Use  um  laço  for  para  imprimir  uma  mensagem  "O  produto  [nome]  está disponível" ou "O produto [nome] está indisponível".

# Resolvi fazer essa em Português Brasileiro para ficar mais legível

produtos={
  "nome": "X-Bacon",
  "preco": 18.00,
  "disponivel": False,
  # Honra ao HubCheff
}

print(f"\nProdutos e suas Disponibilidades\n")
for informacao in produtos: # percorre o dicionário verificando os produtos disponíveis
  if informacao == "disponivel": # verifica se chegou na chave "disponivel"
    if produtos["disponivel"] == False: # se a chave "disponivel" tem como valor "False", então:
      print(f"O produto {produtos["nome"]} não está disponível")
    else:
      print(f"O produto {produtos["nome"]} está disponível")
# Lucas dos Santos Siqueira