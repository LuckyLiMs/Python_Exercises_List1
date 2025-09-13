# Lucas dos Santos Siqueira
# 47 - Crie um dicionário com chaves sendo números e valores sendo seus quadrados. Use um laço for para preencher este dicionário de 1 a 10. 

# Resolvi fazer essa em Português Brasileiro para ficar mais legível

numerosAoQuadrado={
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
}

print(f"\nNúmeros ao Quadrado\n")
for numero in numerosAoQuadrado:
    quadrado = numero ** 2
    numerosAoQuadrado[numero] = quadrado
    print(f"Número: {numero}\nQuadrado: {numerosAoQuadrado[numero]}")
# Lucas dos Santos Siqueira