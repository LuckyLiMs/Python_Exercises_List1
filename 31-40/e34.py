# Lucas dos Santos Siqueira
# 34 - Crie um dicionário com 5 produtos e seus preços. Use um laço for para calcular e imprimir o valor total da compra de todos os produtos.

products={
    # "name" : ["X-Bacon","X-Picanha","X-Tudo","X-Salada","X-Frango"],
    # "price" : [18.00, 25.00, 25.00, 20.00, 22.00],
    "X-Bacon" : 18.00,
    "X-Picanha" : 25.00,
    "X-Tudo" : 25.00,
    "X-Salada" : 20.00,
    "X-Frango" : 22.00,
    # Honra ao HubCheff
}

total = 0
for data in products:
    total += products[data]
print(f"O valor total da compra de todos produtos é de R$:{total:.2f}") # O ":.2f faz o valor ser impresso em uma forma monetária, o f vai formatar como float e o 2 seria com duas casas decimais"
# Lucas dos Santos Siqueira