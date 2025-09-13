# Lucas dos Santos Siqueira
# 49 - Crie  um  dicionário  aninhado,  onde  a  chave  é  o  nome  de  um  país  e  o  valor  é outro  dicionário com as  chaves:  capital  e  população.  Use  laços  for aninhados para imprimir a capital de todos os países.

# Resolvi fazer essa em Português Brasileiro para ficar mais legível

paises = {
  "Brasil": { "Capital" : "Brasília", "Populacao" : 203000000},
  "Canadá": {"Capital" : "Ottawa", "Populacao" : 40000000},
  "Noruega": {"Capital" : "Oslo", "Populacao" : 5500000},
}

print(f"\nPaíses e suas Capitais e Populações\n")
for pais in paises:
  dados = paises[pais]
  print(f"País: {pais}\nCapital: {dados['Capital']}\nPopulação: {dados['Populacao']}\n")
# Lucas dos Santos Siqueira