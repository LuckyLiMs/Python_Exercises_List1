# Lucas dos Santos Siqueira
# 45 - Crie  um  dicionário  que  armazene  o  estoque  de  uma  loja,  com  o  nome  do produto como chave e a quantidade como valor. Use um laço for para imprimir a  mensagem  'Estoque  baixo!'  para  todos  os  produtos  com  menos  de  10 unidades. 

# Resolvi fazer essa em Português Brasileiro para ficar mais legível

estoque={
  "Pão de hambúrguer": 120,
  "Carne bovina (hambúrguer)": 80,
  "Frango empanado": 5,
  "Queijo cheddar": 100,
  "Bacon": 7,
  "Alface": 40,
  "Tomate": 9,
  "Batata frita": 5,
  "Refrigerante (lata)": 2,
  "Molho especial": 25
  # Honra ao HubCheff
}

print(f"\nEstoque\n")
for insumo in estoque:
    if estoque[insumo] < 10:
      print(f"Insumo: {insumo}\nQuantidade: {estoque[insumo]} (Estoque baixo!)\n")
    else:
      print(f"Insumo: {insumo}\nQuantidade: {estoque[insumo]}\n")

# Lucas dos Santos Siqueira