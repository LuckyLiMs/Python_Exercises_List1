# Lucas dos Santos Siqueira
# 46 - Crie  um  dicionário  que  contenha  os  nomes  de  5  funcionários  e  seus  salários. Use um laço for para dar um aumento de 10% para cada funcionário e imprimir o novo salário. 

# Resolvi fazer essa em Português Brasileiro para ficar mais legível

funcionarios={
  "Rojer": 3500,
  "José": 2400,
  "Mané": 1250,
  "Amanda": 600,
  "Nascimento": 7000,
}

print(f"\nFuncionarios com aumento de 10%\n")
for pessoa in funcionarios:
    aumento = funcionarios[pessoa] + (funcionarios[pessoa] * 0.10)
    print(f"Nome: {pessoa}\nSalário com aumento de 10%: {aumento}")
# Lucas dos Santos Siqueira